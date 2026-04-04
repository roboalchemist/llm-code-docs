# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1beta

Title: appengine package - google.golang.org/api/appengine/v1beta - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1beta

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
appengine
 
v1beta
appengine
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 3
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

Package appengine provides access to the App Engine Admin API.

For product documentation, see: https://cloud.google.com/appengine/docs/admin-api/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/appengine/v1beta"
...
ctx := context.Background()
appengineService, err := appengine.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use google.golang.org/api/option.WithScopes:

appengineService, err := appengine.NewService(ctx, option.WithScopes(appengine.CloudPlatformReadOnlyScope))


To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

appengineService, err := appengine.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
appengineService, err := appengine.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type APIService
func New(client *http.Client) (*APIService, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*APIService, error)
type ApiConfigHandler
func (s ApiConfigHandler) MarshalJSON() ([]byte, error)
type ApiEndpointHandler
func (s ApiEndpointHandler) MarshalJSON() ([]byte, error)
type Application
func (s Application) MarshalJSON() ([]byte, error)
type AppsAuthorizedCertificatesCreateCall
func (c *AppsAuthorizedCertificatesCreateCall) Context(ctx context.Context) *AppsAuthorizedCertificatesCreateCall
func (c *AppsAuthorizedCertificatesCreateCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)
func (c *AppsAuthorizedCertificatesCreateCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesCreateCall
func (c *AppsAuthorizedCertificatesCreateCall) Header() http.Header
type AppsAuthorizedCertificatesDeleteCall
func (c *AppsAuthorizedCertificatesDeleteCall) Context(ctx context.Context) *AppsAuthorizedCertificatesDeleteCall
func (c *AppsAuthorizedCertificatesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *AppsAuthorizedCertificatesDeleteCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesDeleteCall
func (c *AppsAuthorizedCertificatesDeleteCall) Header() http.Header
type AppsAuthorizedCertificatesGetCall
func (c *AppsAuthorizedCertificatesGetCall) Context(ctx context.Context) *AppsAuthorizedCertificatesGetCall
func (c *AppsAuthorizedCertificatesGetCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)
func (c *AppsAuthorizedCertificatesGetCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesGetCall
func (c *AppsAuthorizedCertificatesGetCall) Header() http.Header
func (c *AppsAuthorizedCertificatesGetCall) IfNoneMatch(entityTag string) *AppsAuthorizedCertificatesGetCall
func (c *AppsAuthorizedCertificatesGetCall) View(view string) *AppsAuthorizedCertificatesGetCall
type AppsAuthorizedCertificatesListCall
func (c *AppsAuthorizedCertificatesListCall) Context(ctx context.Context) *AppsAuthorizedCertificatesListCall
func (c *AppsAuthorizedCertificatesListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedCertificatesResponse, error)
func (c *AppsAuthorizedCertificatesListCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesListCall
func (c *AppsAuthorizedCertificatesListCall) Header() http.Header
func (c *AppsAuthorizedCertificatesListCall) IfNoneMatch(entityTag string) *AppsAuthorizedCertificatesListCall
func (c *AppsAuthorizedCertificatesListCall) PageSize(pageSize int64) *AppsAuthorizedCertificatesListCall
func (c *AppsAuthorizedCertificatesListCall) PageToken(pageToken string) *AppsAuthorizedCertificatesListCall
func (c *AppsAuthorizedCertificatesListCall) Pages(ctx context.Context, f func(*ListAuthorizedCertificatesResponse) error) error
func (c *AppsAuthorizedCertificatesListCall) View(view string) *AppsAuthorizedCertificatesListCall
type AppsAuthorizedCertificatesPatchCall
func (c *AppsAuthorizedCertificatesPatchCall) Context(ctx context.Context) *AppsAuthorizedCertificatesPatchCall
func (c *AppsAuthorizedCertificatesPatchCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)
func (c *AppsAuthorizedCertificatesPatchCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesPatchCall
func (c *AppsAuthorizedCertificatesPatchCall) Header() http.Header
func (c *AppsAuthorizedCertificatesPatchCall) UpdateMask(updateMask string) *AppsAuthorizedCertificatesPatchCall
type AppsAuthorizedCertificatesService
func NewAppsAuthorizedCertificatesService(s *APIService) *AppsAuthorizedCertificatesService
func (r *AppsAuthorizedCertificatesService) Create(appsId string, authorizedcertificate *AuthorizedCertificate) *AppsAuthorizedCertificatesCreateCall
func (r *AppsAuthorizedCertificatesService) Delete(appsId string, authorizedCertificatesId string) *AppsAuthorizedCertificatesDeleteCall
func (r *AppsAuthorizedCertificatesService) Get(appsId string, authorizedCertificatesId string) *AppsAuthorizedCertificatesGetCall
func (r *AppsAuthorizedCertificatesService) List(appsId string) *AppsAuthorizedCertificatesListCall
func (r *AppsAuthorizedCertificatesService) Patch(appsId string, authorizedCertificatesId string, ...) *AppsAuthorizedCertificatesPatchCall
type AppsAuthorizedDomainsListCall
func (c *AppsAuthorizedDomainsListCall) Context(ctx context.Context) *AppsAuthorizedDomainsListCall
func (c *AppsAuthorizedDomainsListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedDomainsResponse, error)
func (c *AppsAuthorizedDomainsListCall) Fields(s ...googleapi.Field) *AppsAuthorizedDomainsListCall
func (c *AppsAuthorizedDomainsListCall) Header() http.Header
func (c *AppsAuthorizedDomainsListCall) IfNoneMatch(entityTag string) *AppsAuthorizedDomainsListCall
func (c *AppsAuthorizedDomainsListCall) PageSize(pageSize int64) *AppsAuthorizedDomainsListCall
func (c *AppsAuthorizedDomainsListCall) PageToken(pageToken string) *AppsAuthorizedDomainsListCall
func (c *AppsAuthorizedDomainsListCall) Pages(ctx context.Context, f func(*ListAuthorizedDomainsResponse) error) error
type AppsAuthorizedDomainsService
func NewAppsAuthorizedDomainsService(s *APIService) *AppsAuthorizedDomainsService
func (r *AppsAuthorizedDomainsService) List(appsId string) *AppsAuthorizedDomainsListCall
type AppsCreateCall
func (c *AppsCreateCall) Context(ctx context.Context) *AppsCreateCall
func (c *AppsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsCreateCall) Fields(s ...googleapi.Field) *AppsCreateCall
func (c *AppsCreateCall) Header() http.Header
type AppsDomainMappingsCreateCall
func (c *AppsDomainMappingsCreateCall) Context(ctx context.Context) *AppsDomainMappingsCreateCall
func (c *AppsDomainMappingsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsDomainMappingsCreateCall) Fields(s ...googleapi.Field) *AppsDomainMappingsCreateCall
func (c *AppsDomainMappingsCreateCall) Header() http.Header
func (c *AppsDomainMappingsCreateCall) OverrideStrategy(overrideStrategy string) *AppsDomainMappingsCreateCall
type AppsDomainMappingsDeleteCall
func (c *AppsDomainMappingsDeleteCall) Context(ctx context.Context) *AppsDomainMappingsDeleteCall
func (c *AppsDomainMappingsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsDomainMappingsDeleteCall) Fields(s ...googleapi.Field) *AppsDomainMappingsDeleteCall
func (c *AppsDomainMappingsDeleteCall) Header() http.Header
type AppsDomainMappingsGetCall
func (c *AppsDomainMappingsGetCall) Context(ctx context.Context) *AppsDomainMappingsGetCall
func (c *AppsDomainMappingsGetCall) Do(opts ...googleapi.CallOption) (*DomainMapping, error)
func (c *AppsDomainMappingsGetCall) Fields(s ...googleapi.Field) *AppsDomainMappingsGetCall
func (c *AppsDomainMappingsGetCall) Header() http.Header
func (c *AppsDomainMappingsGetCall) IfNoneMatch(entityTag string) *AppsDomainMappingsGetCall
type AppsDomainMappingsListCall
func (c *AppsDomainMappingsListCall) Context(ctx context.Context) *AppsDomainMappingsListCall
func (c *AppsDomainMappingsListCall) Do(opts ...googleapi.CallOption) (*ListDomainMappingsResponse, error)
func (c *AppsDomainMappingsListCall) Fields(s ...googleapi.Field) *AppsDomainMappingsListCall
func (c *AppsDomainMappingsListCall) Header() http.Header
func (c *AppsDomainMappingsListCall) IfNoneMatch(entityTag string) *AppsDomainMappingsListCall
func (c *AppsDomainMappingsListCall) PageSize(pageSize int64) *AppsDomainMappingsListCall
func (c *AppsDomainMappingsListCall) PageToken(pageToken string) *AppsDomainMappingsListCall
func (c *AppsDomainMappingsListCall) Pages(ctx context.Context, f func(*ListDomainMappingsResponse) error) error
type AppsDomainMappingsPatchCall
func (c *AppsDomainMappingsPatchCall) Context(ctx context.Context) *AppsDomainMappingsPatchCall
func (c *AppsDomainMappingsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsDomainMappingsPatchCall) Fields(s ...googleapi.Field) *AppsDomainMappingsPatchCall
func (c *AppsDomainMappingsPatchCall) Header() http.Header
func (c *AppsDomainMappingsPatchCall) UpdateMask(updateMask string) *AppsDomainMappingsPatchCall
type AppsDomainMappingsService
func NewAppsDomainMappingsService(s *APIService) *AppsDomainMappingsService
func (r *AppsDomainMappingsService) Create(appsId string, domainmapping *DomainMapping) *AppsDomainMappingsCreateCall
func (r *AppsDomainMappingsService) Delete(appsId string, domainMappingsId string) *AppsDomainMappingsDeleteCall
func (r *AppsDomainMappingsService) Get(appsId string, domainMappingsId string) *AppsDomainMappingsGetCall
func (r *AppsDomainMappingsService) List(appsId string) *AppsDomainMappingsListCall
func (r *AppsDomainMappingsService) Patch(appsId string, domainMappingsId string, domainmapping *DomainMapping) *AppsDomainMappingsPatchCall
type AppsFirewallIngressRulesBatchUpdateCall
func (c *AppsFirewallIngressRulesBatchUpdateCall) Context(ctx context.Context) *AppsFirewallIngressRulesBatchUpdateCall
func (c *AppsFirewallIngressRulesBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateIngressRulesResponse, error)
func (c *AppsFirewallIngressRulesBatchUpdateCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesBatchUpdateCall
func (c *AppsFirewallIngressRulesBatchUpdateCall) Header() http.Header
type AppsFirewallIngressRulesCreateCall
func (c *AppsFirewallIngressRulesCreateCall) Context(ctx context.Context) *AppsFirewallIngressRulesCreateCall
func (c *AppsFirewallIngressRulesCreateCall) Do(opts ...googleapi.CallOption) (*FirewallRule, error)
func (c *AppsFirewallIngressRulesCreateCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesCreateCall
func (c *AppsFirewallIngressRulesCreateCall) Header() http.Header
type AppsFirewallIngressRulesDeleteCall
func (c *AppsFirewallIngressRulesDeleteCall) Context(ctx context.Context) *AppsFirewallIngressRulesDeleteCall
func (c *AppsFirewallIngressRulesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *AppsFirewallIngressRulesDeleteCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesDeleteCall
func (c *AppsFirewallIngressRulesDeleteCall) Header() http.Header
type AppsFirewallIngressRulesGetCall
func (c *AppsFirewallIngressRulesGetCall) Context(ctx context.Context) *AppsFirewallIngressRulesGetCall
func (c *AppsFirewallIngressRulesGetCall) Do(opts ...googleapi.CallOption) (*FirewallRule, error)
func (c *AppsFirewallIngressRulesGetCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesGetCall
func (c *AppsFirewallIngressRulesGetCall) Header() http.Header
func (c *AppsFirewallIngressRulesGetCall) IfNoneMatch(entityTag string) *AppsFirewallIngressRulesGetCall
type AppsFirewallIngressRulesListCall
func (c *AppsFirewallIngressRulesListCall) Context(ctx context.Context) *AppsFirewallIngressRulesListCall
func (c *AppsFirewallIngressRulesListCall) Do(opts ...googleapi.CallOption) (*ListIngressRulesResponse, error)
func (c *AppsFirewallIngressRulesListCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesListCall
func (c *AppsFirewallIngressRulesListCall) Header() http.Header
func (c *AppsFirewallIngressRulesListCall) IfNoneMatch(entityTag string) *AppsFirewallIngressRulesListCall
func (c *AppsFirewallIngressRulesListCall) MatchingAddress(matchingAddress string) *AppsFirewallIngressRulesListCall
func (c *AppsFirewallIngressRulesListCall) PageSize(pageSize int64) *AppsFirewallIngressRulesListCall
func (c *AppsFirewallIngressRulesListCall) PageToken(pageToken string) *AppsFirewallIngressRulesListCall
func (c *AppsFirewallIngressRulesListCall) Pages(ctx context.Context, f func(*ListIngressRulesResponse) error) error
type AppsFirewallIngressRulesPatchCall
func (c *AppsFirewallIngressRulesPatchCall) Context(ctx context.Context) *AppsFirewallIngressRulesPatchCall
func (c *AppsFirewallIngressRulesPatchCall) Do(opts ...googleapi.CallOption) (*FirewallRule, error)
func (c *AppsFirewallIngressRulesPatchCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesPatchCall
func (c *AppsFirewallIngressRulesPatchCall) Header() http.Header
func (c *AppsFirewallIngressRulesPatchCall) UpdateMask(updateMask string) *AppsFirewallIngressRulesPatchCall
type AppsFirewallIngressRulesService
func NewAppsFirewallIngressRulesService(s *APIService) *AppsFirewallIngressRulesService
func (r *AppsFirewallIngressRulesService) BatchUpdate(appsId string, batchupdateingressrulesrequest *BatchUpdateIngressRulesRequest) *AppsFirewallIngressRulesBatchUpdateCall
func (r *AppsFirewallIngressRulesService) Create(appsId string, firewallrule *FirewallRule) *AppsFirewallIngressRulesCreateCall
func (r *AppsFirewallIngressRulesService) Delete(appsId string, ingressRulesId string) *AppsFirewallIngressRulesDeleteCall
func (r *AppsFirewallIngressRulesService) Get(appsId string, ingressRulesId string) *AppsFirewallIngressRulesGetCall
func (r *AppsFirewallIngressRulesService) List(appsId string) *AppsFirewallIngressRulesListCall
func (r *AppsFirewallIngressRulesService) Patch(appsId string, ingressRulesId string, firewallrule *FirewallRule) *AppsFirewallIngressRulesPatchCall
type AppsFirewallService
func NewAppsFirewallService(s *APIService) *AppsFirewallService
type AppsGetCall
func (c *AppsGetCall) Context(ctx context.Context) *AppsGetCall
func (c *AppsGetCall) Do(opts ...googleapi.CallOption) (*Application, error)
func (c *AppsGetCall) Fields(s ...googleapi.Field) *AppsGetCall
func (c *AppsGetCall) Header() http.Header
func (c *AppsGetCall) IfNoneMatch(entityTag string) *AppsGetCall
func (c *AppsGetCall) IncludeExtraData(includeExtraData string) *AppsGetCall
type AppsListRuntimesCall
func (c *AppsListRuntimesCall) Context(ctx context.Context) *AppsListRuntimesCall
func (c *AppsListRuntimesCall) Do(opts ...googleapi.CallOption) (*ListRuntimesResponse, error)
func (c *AppsListRuntimesCall) Environment(environment string) *AppsListRuntimesCall
func (c *AppsListRuntimesCall) Fields(s ...googleapi.Field) *AppsListRuntimesCall
func (c *AppsListRuntimesCall) Header() http.Header
func (c *AppsListRuntimesCall) IfNoneMatch(entityTag string) *AppsListRuntimesCall
type AppsLocationsGetCall
func (c *AppsLocationsGetCall) Context(ctx context.Context) *AppsLocationsGetCall
func (c *AppsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)
func (c *AppsLocationsGetCall) Fields(s ...googleapi.Field) *AppsLocationsGetCall
func (c *AppsLocationsGetCall) Header() http.Header
func (c *AppsLocationsGetCall) IfNoneMatch(entityTag string) *AppsLocationsGetCall
type AppsLocationsListCall
func (c *AppsLocationsListCall) Context(ctx context.Context) *AppsLocationsListCall
func (c *AppsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)
func (c *AppsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *AppsLocationsListCall
func (c *AppsLocationsListCall) Fields(s ...googleapi.Field) *AppsLocationsListCall
func (c *AppsLocationsListCall) Filter(filter string) *AppsLocationsListCall
func (c *AppsLocationsListCall) Header() http.Header
func (c *AppsLocationsListCall) IfNoneMatch(entityTag string) *AppsLocationsListCall
func (c *AppsLocationsListCall) PageSize(pageSize int64) *AppsLocationsListCall
func (c *AppsLocationsListCall) PageToken(pageToken string) *AppsLocationsListCall
func (c *AppsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error
type AppsLocationsService
func NewAppsLocationsService(s *APIService) *AppsLocationsService
func (r *AppsLocationsService) Get(appsId string, locationsId string) *AppsLocationsGetCall
func (r *AppsLocationsService) List(appsId string) *AppsLocationsListCall
type AppsOperationsGetCall
func (c *AppsOperationsGetCall) Context(ctx context.Context) *AppsOperationsGetCall
func (c *AppsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsOperationsGetCall) Fields(s ...googleapi.Field) *AppsOperationsGetCall
func (c *AppsOperationsGetCall) Header() http.Header
func (c *AppsOperationsGetCall) IfNoneMatch(entityTag string) *AppsOperationsGetCall
type AppsOperationsListCall
func (c *AppsOperationsListCall) Context(ctx context.Context) *AppsOperationsListCall
func (c *AppsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)
func (c *AppsOperationsListCall) Fields(s ...googleapi.Field) *AppsOperationsListCall
func (c *AppsOperationsListCall) Filter(filter string) *AppsOperationsListCall
func (c *AppsOperationsListCall) Header() http.Header
func (c *AppsOperationsListCall) IfNoneMatch(entityTag string) *AppsOperationsListCall
func (c *AppsOperationsListCall) PageSize(pageSize int64) *AppsOperationsListCall
func (c *AppsOperationsListCall) PageToken(pageToken string) *AppsOperationsListCall
func (c *AppsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error
func (c *AppsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *AppsOperationsListCall
type AppsOperationsService
func NewAppsOperationsService(s *APIService) *AppsOperationsService
func (r *AppsOperationsService) Get(appsId string, operationsId string) *AppsOperationsGetCall
func (r *AppsOperationsService) List(appsId string) *AppsOperationsListCall
type AppsPatchCall
func (c *AppsPatchCall) Context(ctx context.Context) *AppsPatchCall
func (c *AppsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsPatchCall) Fields(s ...googleapi.Field) *AppsPatchCall
func (c *AppsPatchCall) Header() http.Header
func (c *AppsPatchCall) UpdateMask(updateMask string) *AppsPatchCall
type AppsRepairCall
func (c *AppsRepairCall) Context(ctx context.Context) *AppsRepairCall
func (c *AppsRepairCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsRepairCall) Fields(s ...googleapi.Field) *AppsRepairCall
func (c *AppsRepairCall) Header() http.Header
type AppsService
func NewAppsService(s *APIService) *AppsService
func (r *AppsService) Create(application *Application) *AppsCreateCall
func (r *AppsService) Get(appsId string) *AppsGetCall
func (r *AppsService) ListRuntimes(appsId string) *AppsListRuntimesCall
func (r *AppsService) Patch(appsId string, application *Application) *AppsPatchCall
func (r *AppsService) Repair(appsId string, repairapplicationrequest *RepairApplicationRequest) *AppsRepairCall
type AppsServicesDeleteCall
func (c *AppsServicesDeleteCall) Context(ctx context.Context) *AppsServicesDeleteCall
func (c *AppsServicesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsServicesDeleteCall) Fields(s ...googleapi.Field) *AppsServicesDeleteCall
func (c *AppsServicesDeleteCall) Header() http.Header
type AppsServicesGetCall
func (c *AppsServicesGetCall) Context(ctx context.Context) *AppsServicesGetCall
func (c *AppsServicesGetCall) Do(opts ...googleapi.CallOption) (*Service, error)
func (c *AppsServicesGetCall) Fields(s ...googleapi.Field) *AppsServicesGetCall
func (c *AppsServicesGetCall) Header() http.Header
func (c *AppsServicesGetCall) IfNoneMatch(entityTag string) *AppsServicesGetCall
func (c *AppsServicesGetCall) IncludeExtraData(includeExtraData string) *AppsServicesGetCall
type AppsServicesListCall
func (c *AppsServicesListCall) Context(ctx context.Context) *AppsServicesListCall
func (c *AppsServicesListCall) Do(opts ...googleapi.CallOption) (*ListServicesResponse, error)
func (c *AppsServicesListCall) Fields(s ...googleapi.Field) *AppsServicesListCall
func (c *AppsServicesListCall) Header() http.Header
func (c *AppsServicesListCall) IfNoneMatch(entityTag string) *AppsServicesListCall
func (c *AppsServicesListCall) PageSize(pageSize int64) *AppsServicesListCall
func (c *AppsServicesListCall) PageToken(pageToken string) *AppsServicesListCall
func (c *AppsServicesListCall) Pages(ctx context.Context, f func(*ListServicesResponse) error) error
type AppsServicesPatchCall
func (c *AppsServicesPatchCall) Context(ctx context.Context) *AppsServicesPatchCall
func (c *AppsServicesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsServicesPatchCall) Fields(s ...googleapi.Field) *AppsServicesPatchCall
func (c *AppsServicesPatchCall) Header() http.Header
func (c *AppsServicesPatchCall) MigrateTraffic(migrateTraffic bool) *AppsServicesPatchCall
func (c *AppsServicesPatchCall) UpdateMask(updateMask string) *AppsServicesPatchCall
type AppsServicesService
func NewAppsServicesService(s *APIService) *AppsServicesService
func (r *AppsServicesService) Delete(appsId string, servicesId string) *AppsServicesDeleteCall
func (r *AppsServicesService) Get(appsId string, servicesId string) *AppsServicesGetCall
func (r *AppsServicesService) List(appsId string) *AppsServicesListCall
func (r *AppsServicesService) Patch(appsId string, servicesId string, service *Service) *AppsServicesPatchCall
type AppsServicesVersionsCreateCall
func (c *AppsServicesVersionsCreateCall) Context(ctx context.Context) *AppsServicesVersionsCreateCall
func (c *AppsServicesVersionsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsServicesVersionsCreateCall) Fields(s ...googleapi.Field) *AppsServicesVersionsCreateCall
func (c *AppsServicesVersionsCreateCall) Header() http.Header
type AppsServicesVersionsDeleteCall
func (c *AppsServicesVersionsDeleteCall) Context(ctx context.Context) *AppsServicesVersionsDeleteCall
func (c *AppsServicesVersionsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsServicesVersionsDeleteCall) Fields(s ...googleapi.Field) *AppsServicesVersionsDeleteCall
func (c *AppsServicesVersionsDeleteCall) Header() http.Header
type AppsServicesVersionsGetCall
func (c *AppsServicesVersionsGetCall) Context(ctx context.Context) *AppsServicesVersionsGetCall
func (c *AppsServicesVersionsGetCall) Do(opts ...googleapi.CallOption) (*Version, error)
func (c *AppsServicesVersionsGetCall) Fields(s ...googleapi.Field) *AppsServicesVersionsGetCall
func (c *AppsServicesVersionsGetCall) Header() http.Header
func (c *AppsServicesVersionsGetCall) IfNoneMatch(entityTag string) *AppsServicesVersionsGetCall
func (c *AppsServicesVersionsGetCall) IncludeExtraData(includeExtraData string) *AppsServicesVersionsGetCall
func (c *AppsServicesVersionsGetCall) View(view string) *AppsServicesVersionsGetCall
type AppsServicesVersionsInstancesDebugCall
func (c *AppsServicesVersionsInstancesDebugCall) Context(ctx context.Context) *AppsServicesVersionsInstancesDebugCall
func (c *AppsServicesVersionsInstancesDebugCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsServicesVersionsInstancesDebugCall) Fields(s ...googleapi.Field) *AppsServicesVersionsInstancesDebugCall
func (c *AppsServicesVersionsInstancesDebugCall) Header() http.Header
type AppsServicesVersionsInstancesDeleteCall
func (c *AppsServicesVersionsInstancesDeleteCall) Context(ctx context.Context) *AppsServicesVersionsInstancesDeleteCall
func (c *AppsServicesVersionsInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsServicesVersionsInstancesDeleteCall) Fields(s ...googleapi.Field) *AppsServicesVersionsInstancesDeleteCall
func (c *AppsServicesVersionsInstancesDeleteCall) Header() http.Header
type AppsServicesVersionsInstancesGetCall
func (c *AppsServicesVersionsInstancesGetCall) Context(ctx context.Context) *AppsServicesVersionsInstancesGetCall
func (c *AppsServicesVersionsInstancesGetCall) Do(opts ...googleapi.CallOption) (*Instance, error)
func (c *AppsServicesVersionsInstancesGetCall) Fields(s ...googleapi.Field) *AppsServicesVersionsInstancesGetCall
func (c *AppsServicesVersionsInstancesGetCall) Header() http.Header
func (c *AppsServicesVersionsInstancesGetCall) IfNoneMatch(entityTag string) *AppsServicesVersionsInstancesGetCall
type AppsServicesVersionsInstancesListCall
func (c *AppsServicesVersionsInstancesListCall) Context(ctx context.Context) *AppsServicesVersionsInstancesListCall
func (c *AppsServicesVersionsInstancesListCall) Do(opts ...googleapi.CallOption) (*ListInstancesResponse, error)
func (c *AppsServicesVersionsInstancesListCall) Fields(s ...googleapi.Field) *AppsServicesVersionsInstancesListCall
func (c *AppsServicesVersionsInstancesListCall) Header() http.Header
func (c *AppsServicesVersionsInstancesListCall) IfNoneMatch(entityTag string) *AppsServicesVersionsInstancesListCall
func (c *AppsServicesVersionsInstancesListCall) PageSize(pageSize int64) *AppsServicesVersionsInstancesListCall
func (c *AppsServicesVersionsInstancesListCall) PageToken(pageToken string) *AppsServicesVersionsInstancesListCall
func (c *AppsServicesVersionsInstancesListCall) Pages(ctx context.Context, f func(*ListInstancesResponse) error) error
type AppsServicesVersionsInstancesService
func NewAppsServicesVersionsInstancesService(s *APIService) *AppsServicesVersionsInstancesService
func (r *AppsServicesVersionsInstancesService) Debug(appsId string, servicesId string, versionsId string, instancesId string, ...) *AppsServicesVersionsInstancesDebugCall
func (r *AppsServicesVersionsInstancesService) Delete(appsId string, servicesId string, versionsId string, instancesId string) *AppsServicesVersionsInstancesDeleteCall
func (r *AppsServicesVersionsInstancesService) Get(appsId string, servicesId string, versionsId string, instancesId string) *AppsServicesVersionsInstancesGetCall
func (r *AppsServicesVersionsInstancesService) List(appsId string, servicesId string, versionsId string) *AppsServicesVersionsInstancesListCall
type AppsServicesVersionsListCall
func (c *AppsServicesVersionsListCall) Context(ctx context.Context) *AppsServicesVersionsListCall
func (c *AppsServicesVersionsListCall) Do(opts ...googleapi.CallOption) (*ListVersionsResponse, error)
func (c *AppsServicesVersionsListCall) Fields(s ...googleapi.Field) *AppsServicesVersionsListCall
func (c *AppsServicesVersionsListCall) Header() http.Header
func (c *AppsServicesVersionsListCall) IfNoneMatch(entityTag string) *AppsServicesVersionsListCall
func (c *AppsServicesVersionsListCall) PageSize(pageSize int64) *AppsServicesVersionsListCall
func (c *AppsServicesVersionsListCall) PageToken(pageToken string) *AppsServicesVersionsListCall
func (c *AppsServicesVersionsListCall) Pages(ctx context.Context, f func(*ListVersionsResponse) error) error
func (c *AppsServicesVersionsListCall) View(view string) *AppsServicesVersionsListCall
type AppsServicesVersionsPatchCall
func (c *AppsServicesVersionsPatchCall) Context(ctx context.Context) *AppsServicesVersionsPatchCall
func (c *AppsServicesVersionsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AppsServicesVersionsPatchCall) Fields(s ...googleapi.Field) *AppsServicesVersionsPatchCall
func (c *AppsServicesVersionsPatchCall) Header() http.Header
func (c *AppsServicesVersionsPatchCall) UpdateMask(updateMask string) *AppsServicesVersionsPatchCall
type AppsServicesVersionsService
func NewAppsServicesVersionsService(s *APIService) *AppsServicesVersionsService
func (r *AppsServicesVersionsService) Create(appsId string, servicesId string, version *Version) *AppsServicesVersionsCreateCall
func (r *AppsServicesVersionsService) Delete(appsId string, servicesId string, versionsId string) *AppsServicesVersionsDeleteCall
func (r *AppsServicesVersionsService) Get(appsId string, servicesId string, versionsId string) *AppsServicesVersionsGetCall
func (r *AppsServicesVersionsService) List(appsId string, servicesId string) *AppsServicesVersionsListCall
func (r *AppsServicesVersionsService) Patch(appsId string, servicesId string, versionsId string, version *Version) *AppsServicesVersionsPatchCall
type AuthorizedCertificate
func (s AuthorizedCertificate) MarshalJSON() ([]byte, error)
type AuthorizedDomain
func (s AuthorizedDomain) MarshalJSON() ([]byte, error)
type AutomaticScaling
func (s AutomaticScaling) MarshalJSON() ([]byte, error)
type BasicScaling
func (s BasicScaling) MarshalJSON() ([]byte, error)
type BatchUpdateIngressRulesRequest
func (s BatchUpdateIngressRulesRequest) MarshalJSON() ([]byte, error)
type BatchUpdateIngressRulesResponse
func (s BatchUpdateIngressRulesResponse) MarshalJSON() ([]byte, error)
type BuildInfo
func (s BuildInfo) MarshalJSON() ([]byte, error)
type CertificateRawData
func (s CertificateRawData) MarshalJSON() ([]byte, error)
type CloudBuildOptions
func (s CloudBuildOptions) MarshalJSON() ([]byte, error)
type ContainerInfo
func (s ContainerInfo) MarshalJSON() ([]byte, error)
type ContainerState
func (s ContainerState) MarshalJSON() ([]byte, error)
type CpuUtilization
func (s CpuUtilization) MarshalJSON() ([]byte, error)
func (s *CpuUtilization) UnmarshalJSON(data []byte) error
type CreateVersionMetadataV1
func (s CreateVersionMetadataV1) MarshalJSON() ([]byte, error)
type CreateVersionMetadataV1Alpha
func (s CreateVersionMetadataV1Alpha) MarshalJSON() ([]byte, error)
type CreateVersionMetadataV1Beta
func (s CreateVersionMetadataV1Beta) MarshalJSON() ([]byte, error)
type CustomMetric
func (s CustomMetric) MarshalJSON() ([]byte, error)
func (s *CustomMetric) UnmarshalJSON(data []byte) error
type Date
func (s Date) MarshalJSON() ([]byte, error)
type DebugInstanceRequest
func (s DebugInstanceRequest) MarshalJSON() ([]byte, error)
type Deployment
func (s Deployment) MarshalJSON() ([]byte, error)
type DiskUtilization
func (s DiskUtilization) MarshalJSON() ([]byte, error)
type DomainMapping
func (s DomainMapping) MarshalJSON() ([]byte, error)
type Empty
type EndpointsApiService
func (s EndpointsApiService) MarshalJSON() ([]byte, error)
type Entrypoint
func (s Entrypoint) MarshalJSON() ([]byte, error)
type ErrorHandler
func (s ErrorHandler) MarshalJSON() ([]byte, error)
type FeatureSettings
func (s FeatureSettings) MarshalJSON() ([]byte, error)
type FileInfo
func (s FileInfo) MarshalJSON() ([]byte, error)
type FirewallRule
func (s FirewallRule) MarshalJSON() ([]byte, error)
type FlexibleRuntimeSettings
func (s FlexibleRuntimeSettings) MarshalJSON() ([]byte, error)
type GceTag
func (s GceTag) MarshalJSON() ([]byte, error)
type GoogleAppengineV1betaLocationMetadata
func (s GoogleAppengineV1betaLocationMetadata) MarshalJSON() ([]byte, error)
type HealthCheck
func (s HealthCheck) MarshalJSON() ([]byte, error)
type IdentityAwareProxy
func (s IdentityAwareProxy) MarshalJSON() ([]byte, error)
type Instance
func (s Instance) MarshalJSON() ([]byte, error)
func (s *Instance) UnmarshalJSON(data []byte) error
type Library
func (s Library) MarshalJSON() ([]byte, error)
type ListAuthorizedCertificatesResponse
func (s ListAuthorizedCertificatesResponse) MarshalJSON() ([]byte, error)
type ListAuthorizedDomainsResponse
func (s ListAuthorizedDomainsResponse) MarshalJSON() ([]byte, error)
type ListDomainMappingsResponse
func (s ListDomainMappingsResponse) MarshalJSON() ([]byte, error)
type ListIngressRulesResponse
func (s ListIngressRulesResponse) MarshalJSON() ([]byte, error)
type ListInstancesResponse
func (s ListInstancesResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListOperationsResponse
func (s ListOperationsResponse) MarshalJSON() ([]byte, error)
type ListRuntimesResponse
func (s ListRuntimesResponse) MarshalJSON() ([]byte, error)
type ListServicesResponse
func (s ListServicesResponse) MarshalJSON() ([]byte, error)
type ListVersionsResponse
func (s ListVersionsResponse) MarshalJSON() ([]byte, error)
type LivenessCheck
func (s LivenessCheck) MarshalJSON() ([]byte, error)
type Location
func (s Location) MarshalJSON() ([]byte, error)
type LocationMetadata
func (s LocationMetadata) MarshalJSON() ([]byte, error)
type ManagedCertificate
func (s ManagedCertificate) MarshalJSON() ([]byte, error)
type ManualScaling
func (s ManualScaling) MarshalJSON() ([]byte, error)
type Network
func (s Network) MarshalJSON() ([]byte, error)
type NetworkSettings
func (s NetworkSettings) MarshalJSON() ([]byte, error)
type NetworkUtilization
func (s NetworkUtilization) MarshalJSON() ([]byte, error)
type Operation
func (s Operation) MarshalJSON() ([]byte, error)
type OperationMetadataV1
func (s OperationMetadataV1) MarshalJSON() ([]byte, error)
type OperationMetadataV1Alpha
func (s OperationMetadataV1Alpha) MarshalJSON() ([]byte, error)
type OperationMetadataV1Beta
func (s OperationMetadataV1Beta) MarshalJSON() ([]byte, error)
type ProjectEvent
func (s ProjectEvent) MarshalJSON() ([]byte, error)
type ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Header() http.Header
type ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Header() http.Header
type ProjectsLocationsApplicationsAuthorizedCertificatesGetCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Header() http.Header
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) View(view string) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall
type ProjectsLocationsApplicationsAuthorizedCertificatesListCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedCertificatesResponse, error)
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Header() http.Header
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Pages(ctx context.Context, f func(*ListAuthorizedCertificatesResponse) error) error
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) View(view string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall
type ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Header() http.Header
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall
type ProjectsLocationsApplicationsAuthorizedCertificatesService
func NewProjectsLocationsApplicationsAuthorizedCertificatesService(s *APIService) *ProjectsLocationsApplicationsAuthorizedCertificatesService
func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Create(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall
func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Delete(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall
func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Get(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall
func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) List(projectsId string, locationsId string, applicationsId string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall
func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Patch(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall
type ProjectsLocationsApplicationsAuthorizedDomainsListCall
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedDomainsListCall
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedDomainsResponse, error)
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedDomainsListCall
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Header() http.Header
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsAuthorizedDomainsListCall
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsAuthorizedDomainsListCall
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsAuthorizedDomainsListCall
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Pages(ctx context.Context, f func(*ListAuthorizedDomainsResponse) error) error
type ProjectsLocationsApplicationsAuthorizedDomainsService
func NewProjectsLocationsApplicationsAuthorizedDomainsService(s *APIService) *ProjectsLocationsApplicationsAuthorizedDomainsService
func (r *ProjectsLocationsApplicationsAuthorizedDomainsService) List(projectsId string, locationsId string, applicationsId string) *ProjectsLocationsApplicationsAuthorizedDomainsListCall
type ProjectsLocationsApplicationsDomainMappingsCreateCall
func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsCreateCall
func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsCreateCall
func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Header() http.Header
func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) OverrideStrategy(overrideStrategy string) *ProjectsLocationsApplicationsDomainMappingsCreateCall
type ProjectsLocationsApplicationsDomainMappingsDeleteCall
func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsDeleteCall
func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsDeleteCall
func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Header() http.Header
type ProjectsLocationsApplicationsDomainMappingsGetCall
func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsGetCall
func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Do(opts ...googleapi.CallOption) (*DomainMapping, error)
func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsGetCall
func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Header() http.Header
func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsDomainMappingsGetCall
type ProjectsLocationsApplicationsDomainMappingsListCall
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsListCall
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Do(opts ...googleapi.CallOption) (*ListDomainMappingsResponse, error)
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsListCall
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Header() http.Header
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsDomainMappingsListCall
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsDomainMappingsListCall
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsDomainMappingsListCall
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Pages(ctx context.Context, f func(*ListDomainMappingsResponse) error) error
type ProjectsLocationsApplicationsDomainMappingsPatchCall
func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsPatchCall
func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsPatchCall
func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Header() http.Header
func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsDomainMappingsPatchCall
type ProjectsLocationsApplicationsDomainMappingsService
func NewProjectsLocationsApplicationsDomainMappingsService(s *APIService) *ProjectsLocationsApplicationsDomainMappingsService
func (r *ProjectsLocationsApplicationsDomainMappingsService) Create(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsDomainMappingsCreateCall
func (r *ProjectsLocationsApplicationsDomainMappingsService) Delete(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsDomainMappingsDeleteCall
func (r *ProjectsLocationsApplicationsDomainMappingsService) Get(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsDomainMappingsGetCall
func (r *ProjectsLocationsApplicationsDomainMappingsService) List(projectsId string, locationsId string, applicationsId string) *ProjectsLocationsApplicationsDomainMappingsListCall
func (r *ProjectsLocationsApplicationsDomainMappingsService) Patch(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsDomainMappingsPatchCall
type ProjectsLocationsApplicationsPatchCall
func (c *ProjectsLocationsApplicationsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsPatchCall
func (c *ProjectsLocationsApplicationsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsPatchCall
func (c *ProjectsLocationsApplicationsPatchCall) Header() http.Header
func (c *ProjectsLocationsApplicationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsPatchCall
type ProjectsLocationsApplicationsService
func NewProjectsLocationsApplicationsService(s *APIService) *ProjectsLocationsApplicationsService
func (r *ProjectsLocationsApplicationsService) Patch(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsPatchCall
type ProjectsLocationsApplicationsServicesDeleteCall
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesDeleteCall
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesDeleteCall
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Header() http.Header
type ProjectsLocationsApplicationsServicesPatchCall
func (c *ProjectsLocationsApplicationsServicesPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesPatchCall
func (c *ProjectsLocationsApplicationsServicesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsServicesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesPatchCall
func (c *ProjectsLocationsApplicationsServicesPatchCall) Header() http.Header
func (c *ProjectsLocationsApplicationsServicesPatchCall) MigrateTraffic(migrateTraffic bool) *ProjectsLocationsApplicationsServicesPatchCall
func (c *ProjectsLocationsApplicationsServicesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsServicesPatchCall
type ProjectsLocationsApplicationsServicesService
func NewProjectsLocationsApplicationsServicesService(s *APIService) *ProjectsLocationsApplicationsServicesService
func (r *ProjectsLocationsApplicationsServicesService) Delete(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsServicesDeleteCall
func (r *ProjectsLocationsApplicationsServicesService) Patch(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsServicesPatchCall
type ProjectsLocationsApplicationsServicesVersionsDeleteCall
func (c *ProjectsLocationsApplicationsServicesVersionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesVersionsDeleteCall
func (c *ProjectsLocationsApplicationsServicesVersionsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsServicesVersionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesVersionsDeleteCall
func (c *ProjectsLocationsApplicationsServicesVersionsDeleteCall) Header() http.Header
type ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Header() http.Header
type ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Header() http.Header
type ProjectsLocationsApplicationsServicesVersionsInstancesService
func NewProjectsLocationsApplicationsServicesVersionsInstancesService(s *APIService) *ProjectsLocationsApplicationsServicesVersionsInstancesService
func (r *ProjectsLocationsApplicationsServicesVersionsInstancesService) Debug(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall
func (r *ProjectsLocationsApplicationsServicesVersionsInstancesService) Delete(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall
type ProjectsLocationsApplicationsServicesVersionsPatchCall
func (c *ProjectsLocationsApplicationsServicesVersionsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesVersionsPatchCall
func (c *ProjectsLocationsApplicationsServicesVersionsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsServicesVersionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesVersionsPatchCall
func (c *ProjectsLocationsApplicationsServicesVersionsPatchCall) Header() http.Header
func (c *ProjectsLocationsApplicationsServicesVersionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsServicesVersionsPatchCall
type ProjectsLocationsApplicationsServicesVersionsService
func NewProjectsLocationsApplicationsServicesVersionsService(s *APIService) *ProjectsLocationsApplicationsServicesVersionsService
func (r *ProjectsLocationsApplicationsServicesVersionsService) Delete(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsServicesVersionsDeleteCall
func (r *ProjectsLocationsApplicationsServicesVersionsService) Patch(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsServicesVersionsPatchCall
type ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Header() http.Header
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall
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
func NewProjectsLocationsOperationsService(s *APIService) *ProjectsLocationsOperationsService
func (r *ProjectsLocationsOperationsService) Get(projectsId string, locationsId string, operationsId string) *ProjectsLocationsOperationsGetCall
func (r *ProjectsLocationsOperationsService) List(projectsId string, locationsId string) *ProjectsLocationsOperationsListCall
type ProjectsLocationsService
func NewProjectsLocationsService(s *APIService) *ProjectsLocationsService
func (r *ProjectsLocationsService) Get(projectsId string, locationsId string) *ProjectsLocationsGetCall
func (r *ProjectsLocationsService) List(projectsId string) *ProjectsLocationsListCall
type ProjectsMetadata
func (s ProjectsMetadata) MarshalJSON() ([]byte, error)
type ProjectsService
func NewProjectsService(s *APIService) *ProjectsService
type ReadinessCheck
func (s ReadinessCheck) MarshalJSON() ([]byte, error)
type Reasons
func (s Reasons) MarshalJSON() ([]byte, error)
type RepairApplicationRequest
type RequestUtilization
func (s RequestUtilization) MarshalJSON() ([]byte, error)
type ResourceEvent
func (s ResourceEvent) MarshalJSON() ([]byte, error)
type ResourceRecord
func (s ResourceRecord) MarshalJSON() ([]byte, error)
type Resources
func (s Resources) MarshalJSON() ([]byte, error)
func (s *Resources) UnmarshalJSON(data []byte) error
type Runtime
func (s Runtime) MarshalJSON() ([]byte, error)
type ScriptHandler
func (s ScriptHandler) MarshalJSON() ([]byte, error)
type Service
func (s Service) MarshalJSON() ([]byte, error)
type SslSettings
func (s SslSettings) MarshalJSON() ([]byte, error)
type StandardSchedulerSettings
func (s StandardSchedulerSettings) MarshalJSON() ([]byte, error)
func (s *StandardSchedulerSettings) UnmarshalJSON(data []byte) error
type StaticFilesHandler
func (s StaticFilesHandler) MarshalJSON() ([]byte, error)
type Status
func (s Status) MarshalJSON() ([]byte, error)
type TrafficSplit
func (s TrafficSplit) MarshalJSON() ([]byte, error)
type UrlDispatchRule
func (s UrlDispatchRule) MarshalJSON() ([]byte, error)
type UrlMap
func (s UrlMap) MarshalJSON() ([]byte, error)
type Version
func (s Version) MarshalJSON() ([]byte, error)
type Volume
func (s Volume) MarshalJSON() ([]byte, error)
func (s *Volume) UnmarshalJSON(data []byte) error
type VpcAccess
func (s VpcAccess) MarshalJSON() ([]byte, error)
type VpcAccessConnector
func (s VpcAccessConnector) MarshalJSON() ([]byte, error)
type VpcNetworkInterface
func (s VpcNetworkInterface) MarshalJSON() ([]byte, error)
type ZipInfo
func (s ZipInfo) MarshalJSON() ([]byte, error)
Constants ¶
View Source
const (
	// View and manage your applications deployed on Google App Engine
	AppengineAdminScope = "https://www.googleapis.com/auth/appengine.admin"

	// See, edit, configure, and delete your Google Cloud data and see the email
	// address for your Google Account.
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"

	// View your data across Google Cloud services and see the email address of
	// your Google Account
	CloudPlatformReadOnlyScope = "https://www.googleapis.com/auth/cloud-platform.read-only"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type APIService ¶
type APIService struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Apps *AppsService

	Projects *ProjectsService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
added in v0.3.0
func NewService(ctx context.Context, opts ...option.ClientOption) (*APIService, error)

NewService creates a new APIService.

type ApiConfigHandler ¶
type ApiConfigHandler struct {
	// AuthFailAction: Action to take when users access resources that require
	// authentication. Defaults to redirect.
	//
	// Possible values:
	//   "AUTH_FAIL_ACTION_UNSPECIFIED" - Not specified. AUTH_FAIL_ACTION_REDIRECT
	// is assumed.
	//   "AUTH_FAIL_ACTION_REDIRECT" - Redirects user to "accounts.google.com". The
	// user is redirected back to the application URL after signing in or creating
	// an account.
	//   "AUTH_FAIL_ACTION_UNAUTHORIZED" - Rejects request with a 401 HTTP status
	// code and an error message.
	AuthFailAction string `json:"authFailAction,omitempty"`
	// Login: Level of login required to access this resource. Defaults to
	// optional.
	//
	// Possible values:
	//   "LOGIN_UNSPECIFIED" - Not specified. LOGIN_OPTIONAL is assumed.
	//   "LOGIN_OPTIONAL" - Does not require that the user is signed in.
	//   "LOGIN_ADMIN" - If the user is not signed in, the auth_fail_action is
	// taken. In addition, if the user is not an administrator for the application,
	// they are given an error message regardless of auth_fail_action. If the user
	// is an administrator, the handler proceeds.
	//   "LOGIN_REQUIRED" - If the user has signed in, the handler proceeds
	// normally. Otherwise, the auth_fail_action is taken.
	Login string `json:"login,omitempty"`
	// Script: Path to the script from the application root directory.
	Script string `json:"script,omitempty"`
	// SecurityLevel: Security (HTTPS) enforcement for this URL.
	//
	// Possible values:
	//   "SECURE_UNSPECIFIED" - Not specified.
	//   "SECURE_DEFAULT" - Both HTTP and HTTPS requests with URLs that match the
	// handler succeed without redirects. The application can examine the request
	// to determine which protocol was used, and respond accordingly.
	//   "SECURE_NEVER" - Requests for a URL that match this handler that use HTTPS
	// are automatically redirected to the HTTP equivalent URL.
	//   "SECURE_OPTIONAL" - Both HTTP and HTTPS requests with URLs that match the
	// handler succeed without redirects. The application can examine the request
	// to determine which protocol was used and respond accordingly.
	//   "SECURE_ALWAYS" - Requests for a URL that match this handler that do not
	// use HTTPS are automatically redirected to the HTTPS URL with the same path.
	// Query parameters are reserved for the redirect.
	SecurityLevel string `json:"securityLevel,omitempty"`
	// Url: URL to serve the endpoint at.
	Url string `json:"url,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AuthFailAction") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuthFailAction") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApiConfigHandler: Google Cloud Endpoints (https://cloud.google.com/endpoints) configuration for API handlers.

func (ApiConfigHandler) MarshalJSON ¶
func (s ApiConfigHandler) MarshalJSON() ([]byte, error)
type ApiEndpointHandler ¶
type ApiEndpointHandler struct {
	// ScriptPath: Path to the script from the application root directory.
	ScriptPath string `json:"scriptPath,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ScriptPath") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ScriptPath") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApiEndpointHandler: Uses Google Cloud Endpoints to handle requests.

func (ApiEndpointHandler) MarshalJSON ¶
func (s ApiEndpointHandler) MarshalJSON() ([]byte, error)
type Application ¶
type Application struct {
	// AuthDomain: Google Apps authentication domain that controls which users can
	// access this application.Defaults to open access for any Google Account.
	AuthDomain string `json:"authDomain,omitempty"`
	// CodeBucket: Output only. Google Cloud Storage bucket that can be used for
	// storing files associated with this application. This bucket is associated
	// with the application and can be used by the gcloud deployment
	// commands.@OutputOnly
	CodeBucket string `json:"codeBucket,omitempty"`
	// DatabaseType: The type of the Cloud Firestore or Cloud Datastore database
	// associated with this application.
	//
	// Possible values:
	//   "DATABASE_TYPE_UNSPECIFIED" - Database type is unspecified.
	//   "CLOUD_DATASTORE" - Cloud Datastore
	//   "CLOUD_FIRESTORE" - Cloud Firestore Native
	//   "CLOUD_DATASTORE_COMPATIBILITY" - Cloud Firestore in Datastore Mode
	DatabaseType string `json:"databaseType,omitempty"`
	// DefaultBucket: Output only. Google Cloud Storage bucket that can be used by
	// this application to store content.@OutputOnly
	DefaultBucket string `json:"defaultBucket,omitempty"`
	// DefaultCookieExpiration: Cookie expiration policy for this application.
	DefaultCookieExpiration string `json:"defaultCookieExpiration,omitempty"`
	// DefaultHostname: Output only. Hostname used to reach this application, as
	// resolved by App Engine.@OutputOnly
	DefaultHostname string `json:"defaultHostname,omitempty"`
	// DispatchRules: HTTP path dispatch rules for requests to the application that
	// do not explicitly target a service or version. Rules are order-dependent. Up
	// to 20 dispatch rules can be supported.
	DispatchRules []*UrlDispatchRule `json:"dispatchRules,omitempty"`
	// FeatureSettings: The feature specific settings to be used in the
	// application.
	FeatureSettings *FeatureSettings `json:"featureSettings,omitempty"`
	// GcrDomain: Output only. The Google Container Registry domain used for
	// storing managed build docker images for this application.
	GcrDomain string `json:"gcrDomain,omitempty"`
	// GeneratedCustomerMetadata: Additional Google Generated Customer Metadata,
	// this field won't be provided by default and can be requested by setting the
	// IncludeExtraData field in GetApplicationRequest
	GeneratedCustomerMetadata googleapi.RawMessage `json:"generatedCustomerMetadata,omitempty"`
	Iap                       *IdentityAwareProxy  `json:"iap,omitempty"`
	// Id: Identifier of the Application resource. This identifier is equivalent to
	// the project ID of the Google Cloud Platform project where you want to deploy
	// your application. Example: myapp.
	Id string `json:"id,omitempty"`
	// LocationId: Location from which this application runs. Application instances
	// run out of the data centers in the specified location, which is also where
	// all of the application's end user content is stored.Defaults to
	// us-central.View the list of supported locations
	// (https://cloud.google.com/appengine/docs/locations).
	LocationId string `json:"locationId,omitempty"`
	Name       string `json:"name,omitempty"`
	// ServiceAccount: The service account associated with the application. This is
	// the app-level default identity. If no identity provided during create
	// version, Admin API will fallback to this one.
	ServiceAccount string `json:"serviceAccount,omitempty"`
	// ServingStatus: Serving status of this application.
	//
	// Possible values:
	//   "UNSPECIFIED" - Serving status is unspecified.
	//   "SERVING" - Application is serving.
	//   "USER_DISABLED" - Application has been disabled by the user.
	//   "SYSTEM_DISABLED" - Application has been disabled by the system.
	ServingStatus string `json:"servingStatus,omitempty"`
	// SslPolicy: The SSL policy that will be applied to the application. If set to
	// Modern it will restrict traffic with TLS < 1.2 and allow only Modern Ciphers
	// suite
	//
	// Possible values:
	//   "SSL_POLICY_UNSPECIFIED" - Required by linter. Will work same as DEFAULT
	//   "DEFAULT" - DEFAULT is to allow all TLS versions and cipher suites
	// supported by App Engine
	//   "MODERN" - MODERN is to allow only TLS 1.2 and TLS 1.3 along with Modern
	// cipher suites only
	SslPolicy string `json:"sslPolicy,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AuthDomain") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuthDomain") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Application: An Application resource contains the top-level configuration of an App Engine application.

func (Application) MarshalJSON ¶
func (s Application) MarshalJSON() ([]byte, error)
type AppsAuthorizedCertificatesCreateCall ¶
type AppsAuthorizedCertificatesCreateCall struct {
	// contains filtered or unexported fields
}
func (*AppsAuthorizedCertificatesCreateCall) Context ¶
func (c *AppsAuthorizedCertificatesCreateCall) Context(ctx context.Context) *AppsAuthorizedCertificatesCreateCall

Context sets the context to be used in this call's Do method.

func (*AppsAuthorizedCertificatesCreateCall) Do ¶
func (c *AppsAuthorizedCertificatesCreateCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)

Do executes the "appengine.apps.authorizedCertificates.create" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsAuthorizedCertificatesCreateCall) Fields ¶
func (c *AppsAuthorizedCertificatesCreateCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsAuthorizedCertificatesCreateCall) Header ¶
func (c *AppsAuthorizedCertificatesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsAuthorizedCertificatesDeleteCall ¶
type AppsAuthorizedCertificatesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AppsAuthorizedCertificatesDeleteCall) Context ¶
func (c *AppsAuthorizedCertificatesDeleteCall) Context(ctx context.Context) *AppsAuthorizedCertificatesDeleteCall

Context sets the context to be used in this call's Do method.

func (*AppsAuthorizedCertificatesDeleteCall) Do ¶
func (c *AppsAuthorizedCertificatesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "appengine.apps.authorizedCertificates.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsAuthorizedCertificatesDeleteCall) Fields ¶
func (c *AppsAuthorizedCertificatesDeleteCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsAuthorizedCertificatesDeleteCall) Header ¶
func (c *AppsAuthorizedCertificatesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsAuthorizedCertificatesGetCall ¶
type AppsAuthorizedCertificatesGetCall struct {
	// contains filtered or unexported fields
}
func (*AppsAuthorizedCertificatesGetCall) Context ¶
func (c *AppsAuthorizedCertificatesGetCall) Context(ctx context.Context) *AppsAuthorizedCertificatesGetCall

Context sets the context to be used in this call's Do method.

func (*AppsAuthorizedCertificatesGetCall) Do ¶
func (c *AppsAuthorizedCertificatesGetCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)

Do executes the "appengine.apps.authorizedCertificates.get" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsAuthorizedCertificatesGetCall) Fields ¶
func (c *AppsAuthorizedCertificatesGetCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsAuthorizedCertificatesGetCall) Header ¶
func (c *AppsAuthorizedCertificatesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsAuthorizedCertificatesGetCall) IfNoneMatch ¶
func (c *AppsAuthorizedCertificatesGetCall) IfNoneMatch(entityTag string) *AppsAuthorizedCertificatesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsAuthorizedCertificatesGetCall) View ¶
func (c *AppsAuthorizedCertificatesGetCall) View(view string) *AppsAuthorizedCertificatesGetCall

View sets the optional parameter "view": Controls the set of fields returned in the GET response.

Possible values:

"BASIC_CERTIFICATE" - Basic certificate information, including applicable


domains and expiration date.

"FULL_CERTIFICATE" - The information from BASIC_CERTIFICATE, plus detailed


information on the domain mappings that have this certificate mapped.

type AppsAuthorizedCertificatesListCall ¶
type AppsAuthorizedCertificatesListCall struct {
	// contains filtered or unexported fields
}
func (*AppsAuthorizedCertificatesListCall) Context ¶
func (c *AppsAuthorizedCertificatesListCall) Context(ctx context.Context) *AppsAuthorizedCertificatesListCall

Context sets the context to be used in this call's Do method.

func (*AppsAuthorizedCertificatesListCall) Do ¶
func (c *AppsAuthorizedCertificatesListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedCertificatesResponse, error)

Do executes the "appengine.apps.authorizedCertificates.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuthorizedCertificatesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsAuthorizedCertificatesListCall) Fields ¶
func (c *AppsAuthorizedCertificatesListCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsAuthorizedCertificatesListCall) Header ¶
func (c *AppsAuthorizedCertificatesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsAuthorizedCertificatesListCall) IfNoneMatch ¶
func (c *AppsAuthorizedCertificatesListCall) IfNoneMatch(entityTag string) *AppsAuthorizedCertificatesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsAuthorizedCertificatesListCall) PageSize ¶
func (c *AppsAuthorizedCertificatesListCall) PageSize(pageSize int64) *AppsAuthorizedCertificatesListCall

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

func (*AppsAuthorizedCertificatesListCall) PageToken ¶
func (c *AppsAuthorizedCertificatesListCall) PageToken(pageToken string) *AppsAuthorizedCertificatesListCall

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

func (*AppsAuthorizedCertificatesListCall) Pages ¶
func (c *AppsAuthorizedCertificatesListCall) Pages(ctx context.Context, f func(*ListAuthorizedCertificatesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*AppsAuthorizedCertificatesListCall) View ¶
func (c *AppsAuthorizedCertificatesListCall) View(view string) *AppsAuthorizedCertificatesListCall

View sets the optional parameter "view": Controls the set of fields returned in the LIST response.

Possible values:

"BASIC_CERTIFICATE" - Basic certificate information, including applicable


domains and expiration date.

"FULL_CERTIFICATE" - The information from BASIC_CERTIFICATE, plus detailed


information on the domain mappings that have this certificate mapped.

type AppsAuthorizedCertificatesPatchCall ¶
type AppsAuthorizedCertificatesPatchCall struct {
	// contains filtered or unexported fields
}
func (*AppsAuthorizedCertificatesPatchCall) Context ¶
func (c *AppsAuthorizedCertificatesPatchCall) Context(ctx context.Context) *AppsAuthorizedCertificatesPatchCall

Context sets the context to be used in this call's Do method.

func (*AppsAuthorizedCertificatesPatchCall) Do ¶
func (c *AppsAuthorizedCertificatesPatchCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)

Do executes the "appengine.apps.authorizedCertificates.patch" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsAuthorizedCertificatesPatchCall) Fields ¶
func (c *AppsAuthorizedCertificatesPatchCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsAuthorizedCertificatesPatchCall) Header ¶
func (c *AppsAuthorizedCertificatesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsAuthorizedCertificatesPatchCall) UpdateMask ¶
func (c *AppsAuthorizedCertificatesPatchCall) UpdateMask(updateMask string) *AppsAuthorizedCertificatesPatchCall

UpdateMask sets the optional parameter "updateMask": Standard field mask for the set of fields to be updated. Updates are only supported on the certificate_raw_data and display_name fields.

type AppsAuthorizedCertificatesService ¶
type AppsAuthorizedCertificatesService struct {
	// contains filtered or unexported fields
}
func NewAppsAuthorizedCertificatesService ¶
func NewAppsAuthorizedCertificatesService(s *APIService) *AppsAuthorizedCertificatesService
func (*AppsAuthorizedCertificatesService) Create ¶
func (r *AppsAuthorizedCertificatesService) Create(appsId string, authorizedcertificate *AuthorizedCertificate) *AppsAuthorizedCertificatesCreateCall

Create: Uploads the specified SSL certificate.

appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
func (*AppsAuthorizedCertificatesService) Delete ¶
func (r *AppsAuthorizedCertificatesService) Delete(appsId string, authorizedCertificatesId string) *AppsAuthorizedCertificatesDeleteCall

Delete: Deletes the specified SSL certificate.

appsId: Part of `name`. Name of the resource to delete. Example: apps/myapp/authorizedCertificates/12345.
authorizedCertificatesId: Part of `name`. See documentation of `appsId`.
func (*AppsAuthorizedCertificatesService) Get ¶
func (r *AppsAuthorizedCertificatesService) Get(appsId string, authorizedCertificatesId string) *AppsAuthorizedCertificatesGetCall

Get: Gets the specified SSL certificate.

appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/authorizedCertificates/12345.
authorizedCertificatesId: Part of `name`. See documentation of `appsId`.
func (*AppsAuthorizedCertificatesService) List ¶
func (r *AppsAuthorizedCertificatesService) List(appsId string) *AppsAuthorizedCertificatesListCall

List: Lists all SSL certificates the user is authorized to administer.

appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
func (*AppsAuthorizedCertificatesService) Patch ¶
func (r *AppsAuthorizedCertificatesService) Patch(appsId string, authorizedCertificatesId string, authorizedcertificate *AuthorizedCertificate) *AppsAuthorizedCertificatesPatchCall

Patch: Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update certificate_data with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate display_name may also be updated.

appsId: Part of `name`. Name of the resource to update. Example: apps/myapp/authorizedCertificates/12345.
authorizedCertificatesId: Part of `name`. See documentation of `appsId`.
type AppsAuthorizedDomainsListCall ¶
type AppsAuthorizedDomainsListCall struct {
	// contains filtered or unexported fields
}
func (*AppsAuthorizedDomainsListCall) Context ¶
func (c *AppsAuthorizedDomainsListCall) Context(ctx context.Context) *AppsAuthorizedDomainsListCall

Context sets the context to be used in this call's Do method.

func (*AppsAuthorizedDomainsListCall) Do ¶
func (c *AppsAuthorizedDomainsListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedDomainsResponse, error)

Do executes the "appengine.apps.authorizedDomains.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuthorizedDomainsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsAuthorizedDomainsListCall) Fields ¶
func (c *AppsAuthorizedDomainsListCall) Fields(s ...googleapi.Field) *AppsAuthorizedDomainsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsAuthorizedDomainsListCall) Header ¶
func (c *AppsAuthorizedDomainsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsAuthorizedDomainsListCall) IfNoneMatch ¶
func (c *AppsAuthorizedDomainsListCall) IfNoneMatch(entityTag string) *AppsAuthorizedDomainsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsAuthorizedDomainsListCall) PageSize ¶
func (c *AppsAuthorizedDomainsListCall) PageSize(pageSize int64) *AppsAuthorizedDomainsListCall

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

func (*AppsAuthorizedDomainsListCall) PageToken ¶
func (c *AppsAuthorizedDomainsListCall) PageToken(pageToken string) *AppsAuthorizedDomainsListCall

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

func (*AppsAuthorizedDomainsListCall) Pages ¶
func (c *AppsAuthorizedDomainsListCall) Pages(ctx context.Context, f func(*ListAuthorizedDomainsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AppsAuthorizedDomainsService ¶
type AppsAuthorizedDomainsService struct {
	// contains filtered or unexported fields
}
func NewAppsAuthorizedDomainsService ¶
func NewAppsAuthorizedDomainsService(s *APIService) *AppsAuthorizedDomainsService
func (*AppsAuthorizedDomainsService) List ¶
func (r *AppsAuthorizedDomainsService) List(appsId string) *AppsAuthorizedDomainsListCall

List: Lists all domains the user is authorized to administer.

appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
type AppsCreateCall ¶
type AppsCreateCall struct {
	// contains filtered or unexported fields
}
func (*AppsCreateCall) Context ¶
func (c *AppsCreateCall) Context(ctx context.Context) *AppsCreateCall

Context sets the context to be used in this call's Do method.

func (*AppsCreateCall) Do ¶
func (c *AppsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsCreateCall) Fields ¶
func (c *AppsCreateCall) Fields(s ...googleapi.Field) *AppsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsCreateCall) Header ¶
func (c *AppsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsDomainMappingsCreateCall ¶
type AppsDomainMappingsCreateCall struct {
	// contains filtered or unexported fields
}
func (*AppsDomainMappingsCreateCall) Context ¶
func (c *AppsDomainMappingsCreateCall) Context(ctx context.Context) *AppsDomainMappingsCreateCall

Context sets the context to be used in this call's Do method.

func (*AppsDomainMappingsCreateCall) Do ¶
func (c *AppsDomainMappingsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.domainMappings.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsDomainMappingsCreateCall) Fields ¶
func (c *AppsDomainMappingsCreateCall) Fields(s ...googleapi.Field) *AppsDomainMappingsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsDomainMappingsCreateCall) Header ¶
func (c *AppsDomainMappingsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsDomainMappingsCreateCall) OverrideStrategy ¶
func (c *AppsDomainMappingsCreateCall) OverrideStrategy(overrideStrategy string) *AppsDomainMappingsCreateCall

OverrideStrategy sets the optional parameter "overrideStrategy": Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected.

Possible values:

"UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY" - Strategy unspecified. Defaults to


STRICT.

"STRICT" - Overrides not allowed. If a mapping already exists for the


specified domain, the request will return an ALREADY_EXISTS (409).

"OVERRIDE" - Overrides allowed. If a mapping already exists for the


specified domain, the request will overwrite it. Note that this might stop another Google product from serving. For example, if the domain is mapped to another App Engine application, that app will no longer serve from that domain.

type AppsDomainMappingsDeleteCall ¶
type AppsDomainMappingsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AppsDomainMappingsDeleteCall) Context ¶
func (c *AppsDomainMappingsDeleteCall) Context(ctx context.Context) *AppsDomainMappingsDeleteCall

Context sets the context to be used in this call's Do method.

func (*AppsDomainMappingsDeleteCall) Do ¶
func (c *AppsDomainMappingsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.domainMappings.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsDomainMappingsDeleteCall) Fields ¶
func (c *AppsDomainMappingsDeleteCall) Fields(s ...googleapi.Field) *AppsDomainMappingsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsDomainMappingsDeleteCall) Header ¶
func (c *AppsDomainMappingsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsDomainMappingsGetCall ¶
type AppsDomainMappingsGetCall struct {
	// contains filtered or unexported fields
}
func (*AppsDomainMappingsGetCall) Context ¶
func (c *AppsDomainMappingsGetCall) Context(ctx context.Context) *AppsDomainMappingsGetCall

Context sets the context to be used in this call's Do method.

func (*AppsDomainMappingsGetCall) Do ¶
func (c *AppsDomainMappingsGetCall) Do(opts ...googleapi.CallOption) (*DomainMapping, error)

Do executes the "appengine.apps.domainMappings.get" call. Any non-2xx status code is an error. Response headers are in either *DomainMapping.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsDomainMappingsGetCall) Fields ¶
func (c *AppsDomainMappingsGetCall) Fields(s ...googleapi.Field) *AppsDomainMappingsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsDomainMappingsGetCall) Header ¶
func (c *AppsDomainMappingsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsDomainMappingsGetCall) IfNoneMatch ¶
func (c *AppsDomainMappingsGetCall) IfNoneMatch(entityTag string) *AppsDomainMappingsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AppsDomainMappingsListCall ¶
type AppsDomainMappingsListCall struct {
	// contains filtered or unexported fields
}
func (*AppsDomainMappingsListCall) Context ¶
func (c *AppsDomainMappingsListCall) Context(ctx context.Context) *AppsDomainMappingsListCall

Context sets the context to be used in this call's Do method.

func (*AppsDomainMappingsListCall) Do ¶
func (c *AppsDomainMappingsListCall) Do(opts ...googleapi.CallOption) (*ListDomainMappingsResponse, error)

Do executes the "appengine.apps.domainMappings.list" call. Any non-2xx status code is an error. Response headers are in either *ListDomainMappingsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsDomainMappingsListCall) Fields ¶
func (c *AppsDomainMappingsListCall) Fields(s ...googleapi.Field) *AppsDomainMappingsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsDomainMappingsListCall) Header ¶
func (c *AppsDomainMappingsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsDomainMappingsListCall) IfNoneMatch ¶
func (c *AppsDomainMappingsListCall) IfNoneMatch(entityTag string) *AppsDomainMappingsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsDomainMappingsListCall) PageSize ¶
func (c *AppsDomainMappingsListCall) PageSize(pageSize int64) *AppsDomainMappingsListCall

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

func (*AppsDomainMappingsListCall) PageToken ¶
func (c *AppsDomainMappingsListCall) PageToken(pageToken string) *AppsDomainMappingsListCall

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

func (*AppsDomainMappingsListCall) Pages ¶
func (c *AppsDomainMappingsListCall) Pages(ctx context.Context, f func(*ListDomainMappingsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AppsDomainMappingsPatchCall ¶
type AppsDomainMappingsPatchCall struct {
	// contains filtered or unexported fields
}
func (*AppsDomainMappingsPatchCall) Context ¶
func (c *AppsDomainMappingsPatchCall) Context(ctx context.Context) *AppsDomainMappingsPatchCall

Context sets the context to be used in this call's Do method.

func (*AppsDomainMappingsPatchCall) Do ¶
func (c *AppsDomainMappingsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.domainMappings.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsDomainMappingsPatchCall) Fields ¶
func (c *AppsDomainMappingsPatchCall) Fields(s ...googleapi.Field) *AppsDomainMappingsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsDomainMappingsPatchCall) Header ¶
func (c *AppsDomainMappingsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsDomainMappingsPatchCall) UpdateMask ¶
func (c *AppsDomainMappingsPatchCall) UpdateMask(updateMask string) *AppsDomainMappingsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Standard field mask for the set of fields to be updated.

type AppsDomainMappingsService ¶
type AppsDomainMappingsService struct {
	// contains filtered or unexported fields
}
func NewAppsDomainMappingsService ¶
func NewAppsDomainMappingsService(s *APIService) *AppsDomainMappingsService
func (*AppsDomainMappingsService) Create ¶
func (r *AppsDomainMappingsService) Create(appsId string, domainmapping *DomainMapping) *AppsDomainMappingsCreateCall

Create: Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see AuthorizedDomains.ListAuthorizedDomains.

appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
func (*AppsDomainMappingsService) Delete ¶
func (r *AppsDomainMappingsService) Delete(appsId string, domainMappingsId string) *AppsDomainMappingsDeleteCall

Delete: Deletes the specified domain mapping. A user must be authorized to administer the associated domain in order to delete a DomainMapping resource.

appsId: Part of `name`. Name of the resource to delete. Example: apps/myapp/domainMappings/example.com.
domainMappingsId: Part of `name`. See documentation of `appsId`.
func (*AppsDomainMappingsService) Get ¶
func (r *AppsDomainMappingsService) Get(appsId string, domainMappingsId string) *AppsDomainMappingsGetCall

Get: Gets the specified domain mapping.

appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/domainMappings/example.com.
domainMappingsId: Part of `name`. See documentation of `appsId`.
func (*AppsDomainMappingsService) List ¶
func (r *AppsDomainMappingsService) List(appsId string) *AppsDomainMappingsListCall

List: Lists the domain mappings on an application.

appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
func (*AppsDomainMappingsService) Patch ¶
func (r *AppsDomainMappingsService) Patch(appsId string, domainMappingsId string, domainmapping *DomainMapping) *AppsDomainMappingsPatchCall

Patch: Updates the specified domain mapping. To map an SSL certificate to a domain mapping, update certificate_id to point to an AuthorizedCertificate resource. A user must be authorized to administer the associated domain in order to update a DomainMapping resource.

appsId: Part of `name`. Name of the resource to update. Example: apps/myapp/domainMappings/example.com.
domainMappingsId: Part of `name`. See documentation of `appsId`.
type AppsFirewallIngressRulesBatchUpdateCall ¶
type AppsFirewallIngressRulesBatchUpdateCall struct {
	// contains filtered or unexported fields
}
func (*AppsFirewallIngressRulesBatchUpdateCall) Context ¶
func (c *AppsFirewallIngressRulesBatchUpdateCall) Context(ctx context.Context) *AppsFirewallIngressRulesBatchUpdateCall

Context sets the context to be used in this call's Do method.

func (*AppsFirewallIngressRulesBatchUpdateCall) Do ¶
func (c *AppsFirewallIngressRulesBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateIngressRulesResponse, error)

Do executes the "appengine.apps.firewall.ingressRules.batchUpdate" call. Any non-2xx status code is an error. Response headers are in either *BatchUpdateIngressRulesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsFirewallIngressRulesBatchUpdateCall) Fields ¶
func (c *AppsFirewallIngressRulesBatchUpdateCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesBatchUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsFirewallIngressRulesBatchUpdateCall) Header ¶
func (c *AppsFirewallIngressRulesBatchUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsFirewallIngressRulesCreateCall ¶
type AppsFirewallIngressRulesCreateCall struct {
	// contains filtered or unexported fields
}
func (*AppsFirewallIngressRulesCreateCall) Context ¶
func (c *AppsFirewallIngressRulesCreateCall) Context(ctx context.Context) *AppsFirewallIngressRulesCreateCall

Context sets the context to be used in this call's Do method.

func (*AppsFirewallIngressRulesCreateCall) Do ¶
func (c *AppsFirewallIngressRulesCreateCall) Do(opts ...googleapi.CallOption) (*FirewallRule, error)

Do executes the "appengine.apps.firewall.ingressRules.create" call. Any non-2xx status code is an error. Response headers are in either *FirewallRule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsFirewallIngressRulesCreateCall) Fields ¶
func (c *AppsFirewallIngressRulesCreateCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsFirewallIngressRulesCreateCall) Header ¶
func (c *AppsFirewallIngressRulesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsFirewallIngressRulesDeleteCall ¶
type AppsFirewallIngressRulesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AppsFirewallIngressRulesDeleteCall) Context ¶
func (c *AppsFirewallIngressRulesDeleteCall) Context(ctx context.Context) *AppsFirewallIngressRulesDeleteCall

Context sets the context to be used in this call's Do method.

func (*AppsFirewallIngressRulesDeleteCall) Do ¶
func (c *AppsFirewallIngressRulesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "appengine.apps.firewall.ingressRules.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsFirewallIngressRulesDeleteCall) Fields ¶
func (c *AppsFirewallIngressRulesDeleteCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsFirewallIngressRulesDeleteCall) Header ¶
func (c *AppsFirewallIngressRulesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsFirewallIngressRulesGetCall ¶
type AppsFirewallIngressRulesGetCall struct {
	// contains filtered or unexported fields
}
func (*AppsFirewallIngressRulesGetCall) Context ¶
func (c *AppsFirewallIngressRulesGetCall) Context(ctx context.Context) *AppsFirewallIngressRulesGetCall

Context sets the context to be used in this call's Do method.

func (*AppsFirewallIngressRulesGetCall) Do ¶
func (c *AppsFirewallIngressRulesGetCall) Do(opts ...googleapi.CallOption) (*FirewallRule, error)

Do executes the "appengine.apps.firewall.ingressRules.get" call. Any non-2xx status code is an error. Response headers are in either *FirewallRule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsFirewallIngressRulesGetCall) Fields ¶
func (c *AppsFirewallIngressRulesGetCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsFirewallIngressRulesGetCall) Header ¶
func (c *AppsFirewallIngressRulesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsFirewallIngressRulesGetCall) IfNoneMatch ¶
func (c *AppsFirewallIngressRulesGetCall) IfNoneMatch(entityTag string) *AppsFirewallIngressRulesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AppsFirewallIngressRulesListCall ¶
type AppsFirewallIngressRulesListCall struct {
	// contains filtered or unexported fields
}
func (*AppsFirewallIngressRulesListCall) Context ¶
func (c *AppsFirewallIngressRulesListCall) Context(ctx context.Context) *AppsFirewallIngressRulesListCall

Context sets the context to be used in this call's Do method.

func (*AppsFirewallIngressRulesListCall) Do ¶
func (c *AppsFirewallIngressRulesListCall) Do(opts ...googleapi.CallOption) (*ListIngressRulesResponse, error)

Do executes the "appengine.apps.firewall.ingressRules.list" call. Any non-2xx status code is an error. Response headers are in either *ListIngressRulesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsFirewallIngressRulesListCall) Fields ¶
func (c *AppsFirewallIngressRulesListCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsFirewallIngressRulesListCall) Header ¶
func (c *AppsFirewallIngressRulesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsFirewallIngressRulesListCall) IfNoneMatch ¶
func (c *AppsFirewallIngressRulesListCall) IfNoneMatch(entityTag string) *AppsFirewallIngressRulesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsFirewallIngressRulesListCall) MatchingAddress ¶
func (c *AppsFirewallIngressRulesListCall) MatchingAddress(matchingAddress string) *AppsFirewallIngressRulesListCall

MatchingAddress sets the optional parameter "matchingAddress": A valid IP Address. If set, only rules matching this address will be returned. The first returned rule will be the rule that fires on requests from this IP.

func (*AppsFirewallIngressRulesListCall) PageSize ¶
func (c *AppsFirewallIngressRulesListCall) PageSize(pageSize int64) *AppsFirewallIngressRulesListCall

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

func (*AppsFirewallIngressRulesListCall) PageToken ¶
func (c *AppsFirewallIngressRulesListCall) PageToken(pageToken string) *AppsFirewallIngressRulesListCall

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

func (*AppsFirewallIngressRulesListCall) Pages ¶
func (c *AppsFirewallIngressRulesListCall) Pages(ctx context.Context, f func(*ListIngressRulesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AppsFirewallIngressRulesPatchCall ¶
type AppsFirewallIngressRulesPatchCall struct {
	// contains filtered or unexported fields
}
func (*AppsFirewallIngressRulesPatchCall) Context ¶
func (c *AppsFirewallIngressRulesPatchCall) Context(ctx context.Context) *AppsFirewallIngressRulesPatchCall

Context sets the context to be used in this call's Do method.

func (*AppsFirewallIngressRulesPatchCall) Do ¶
func (c *AppsFirewallIngressRulesPatchCall) Do(opts ...googleapi.CallOption) (*FirewallRule, error)

Do executes the "appengine.apps.firewall.ingressRules.patch" call. Any non-2xx status code is an error. Response headers are in either *FirewallRule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsFirewallIngressRulesPatchCall) Fields ¶
func (c *AppsFirewallIngressRulesPatchCall) Fields(s ...googleapi.Field) *AppsFirewallIngressRulesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsFirewallIngressRulesPatchCall) Header ¶
func (c *AppsFirewallIngressRulesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsFirewallIngressRulesPatchCall) UpdateMask ¶
func (c *AppsFirewallIngressRulesPatchCall) UpdateMask(updateMask string) *AppsFirewallIngressRulesPatchCall

UpdateMask sets the optional parameter "updateMask": Standard field mask for the set of fields to be updated.

type AppsFirewallIngressRulesService ¶
type AppsFirewallIngressRulesService struct {
	// contains filtered or unexported fields
}
func NewAppsFirewallIngressRulesService ¶
func NewAppsFirewallIngressRulesService(s *APIService) *AppsFirewallIngressRulesService
func (*AppsFirewallIngressRulesService) BatchUpdate ¶
func (r *AppsFirewallIngressRulesService) BatchUpdate(appsId string, batchupdateingressrulesrequest *BatchUpdateIngressRulesRequest) *AppsFirewallIngressRulesBatchUpdateCall

BatchUpdate: Replaces the entire firewall ruleset in one bulk operation. This overrides and replaces the rules of an existing firewall with the new rules.If the final rule does not match traffic with the '*' wildcard IP range, then an "allow all" rule is explicitly added to the end of the list.

appsId: Part of `name`. Name of the Firewall collection to set. Example: apps/myapp/firewall/ingressRules.
func (*AppsFirewallIngressRulesService) Create ¶
func (r *AppsFirewallIngressRulesService) Create(appsId string, firewallrule *FirewallRule) *AppsFirewallIngressRulesCreateCall

Create: Creates a firewall rule for the application.

appsId: Part of `parent`. Name of the parent Firewall collection in which to create a new rule. Example: apps/myapp/firewall/ingressRules.
func (*AppsFirewallIngressRulesService) Delete ¶
func (r *AppsFirewallIngressRulesService) Delete(appsId string, ingressRulesId string) *AppsFirewallIngressRulesDeleteCall

Delete: Deletes the specified firewall rule.

appsId: Part of `name`. Name of the Firewall resource to delete. Example: apps/myapp/firewall/ingressRules/100.
ingressRulesId: Part of `name`. See documentation of `appsId`.
func (*AppsFirewallIngressRulesService) Get ¶
func (r *AppsFirewallIngressRulesService) Get(appsId string, ingressRulesId string) *AppsFirewallIngressRulesGetCall

Get: Gets the specified firewall rule.

appsId: Part of `name`. Name of the Firewall resource to retrieve. Example: apps/myapp/firewall/ingressRules/100.
ingressRulesId: Part of `name`. See documentation of `appsId`.
func (*AppsFirewallIngressRulesService) List ¶
func (r *AppsFirewallIngressRulesService) List(appsId string) *AppsFirewallIngressRulesListCall

List: Lists the firewall rules of an application.

appsId: Part of `parent`. Name of the Firewall collection to retrieve. Example: apps/myapp/firewall/ingressRules.
func (*AppsFirewallIngressRulesService) Patch ¶
func (r *AppsFirewallIngressRulesService) Patch(appsId string, ingressRulesId string, firewallrule *FirewallRule) *AppsFirewallIngressRulesPatchCall

Patch: Updates the specified firewall rule.

appsId: Part of `name`. Name of the Firewall resource to update. Example: apps/myapp/firewall/ingressRules/100.
ingressRulesId: Part of `name`. See documentation of `appsId`.
type AppsFirewallService ¶
type AppsFirewallService struct {
	IngressRules *AppsFirewallIngressRulesService
	// contains filtered or unexported fields
}
func NewAppsFirewallService ¶
func NewAppsFirewallService(s *APIService) *AppsFirewallService
type AppsGetCall ¶
type AppsGetCall struct {
	// contains filtered or unexported fields
}
func (*AppsGetCall) Context ¶
func (c *AppsGetCall) Context(ctx context.Context) *AppsGetCall

Context sets the context to be used in this call's Do method.

func (*AppsGetCall) Do ¶
func (c *AppsGetCall) Do(opts ...googleapi.CallOption) (*Application, error)

Do executes the "appengine.apps.get" call. Any non-2xx status code is an error. Response headers are in either *Application.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsGetCall) Fields ¶
func (c *AppsGetCall) Fields(s ...googleapi.Field) *AppsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsGetCall) Header ¶
func (c *AppsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsGetCall) IfNoneMatch ¶
func (c *AppsGetCall) IfNoneMatch(entityTag string) *AppsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsGetCall) IncludeExtraData ¶
added in v0.142.0
func (c *AppsGetCall) IncludeExtraData(includeExtraData string) *AppsGetCall

IncludeExtraData sets the optional parameter "includeExtraData": Options to include extra data

Possible values:

"INCLUDE_EXTRA_DATA_UNSPECIFIED" - Unspecified: No extra data will be


returned

"INCLUDE_EXTRA_DATA_NONE" - Do not return any extra data
"INCLUDE_GOOGLE_GENERATED_METADATA" - Return GGCM associated with the


resources

type AppsListRuntimesCall ¶
added in v0.148.0
type AppsListRuntimesCall struct {
	// contains filtered or unexported fields
}
func (*AppsListRuntimesCall) Context ¶
added in v0.148.0
func (c *AppsListRuntimesCall) Context(ctx context.Context) *AppsListRuntimesCall

Context sets the context to be used in this call's Do method.

func (*AppsListRuntimesCall) Do ¶
added in v0.148.0
func (c *AppsListRuntimesCall) Do(opts ...googleapi.CallOption) (*ListRuntimesResponse, error)

Do executes the "appengine.apps.listRuntimes" call. Any non-2xx status code is an error. Response headers are in either *ListRuntimesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsListRuntimesCall) Environment ¶
added in v0.148.0
func (c *AppsListRuntimesCall) Environment(environment string) *AppsListRuntimesCall

Environment sets the optional parameter "environment": The environment of the Application.

Possible values:

"ENVIRONMENT_UNSPECIFIED" - Default value.
"STANDARD" - App Engine Standard.
"FLEXIBLE" - App Engine Flexible

func (*AppsListRuntimesCall) Fields ¶
added in v0.148.0
func (c *AppsListRuntimesCall) Fields(s ...googleapi.Field) *AppsListRuntimesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsListRuntimesCall) Header ¶
added in v0.148.0
func (c *AppsListRuntimesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsListRuntimesCall) IfNoneMatch ¶
added in v0.148.0
func (c *AppsListRuntimesCall) IfNoneMatch(entityTag string) *AppsListRuntimesCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AppsLocationsGetCall ¶
type AppsLocationsGetCall struct {
	// contains filtered or unexported fields
}
func (*AppsLocationsGetCall) Context ¶
func (c *AppsLocationsGetCall) Context(ctx context.Context) *AppsLocationsGetCall

Context sets the context to be used in this call's Do method.

func (*AppsLocationsGetCall) Do ¶
func (c *AppsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)

Do executes the "appengine.apps.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsLocationsGetCall) Fields ¶
func (c *AppsLocationsGetCall) Fields(s ...googleapi.Field) *AppsLocationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsLocationsGetCall) Header ¶
func (c *AppsLocationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsLocationsGetCall) IfNoneMatch ¶
func (c *AppsLocationsGetCall) IfNoneMatch(entityTag string) *AppsLocationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AppsLocationsListCall ¶
type AppsLocationsListCall struct {
	// contains filtered or unexported fields
}
func (*AppsLocationsListCall) Context ¶
func (c *AppsLocationsListCall) Context(ctx context.Context) *AppsLocationsListCall

Context sets the context to be used in this call's Do method.

func (*AppsLocationsListCall) Do ¶
func (c *AppsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)

Do executes the "appengine.apps.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsLocationsListCall) ExtraLocationTypes ¶
added in v0.230.0
func (c *AppsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *AppsLocationsListCall

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

func (*AppsLocationsListCall) Fields ¶
func (c *AppsLocationsListCall) Fields(s ...googleapi.Field) *AppsLocationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsLocationsListCall) Filter ¶
func (c *AppsLocationsListCall) Filter(filter string) *AppsLocationsListCall

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 (https://google.aip.dev/160).

func (*AppsLocationsListCall) Header ¶
func (c *AppsLocationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsLocationsListCall) IfNoneMatch ¶
func (c *AppsLocationsListCall) IfNoneMatch(entityTag string) *AppsLocationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsLocationsListCall) PageSize ¶
func (c *AppsLocationsListCall) PageSize(pageSize int64) *AppsLocationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

func (*AppsLocationsListCall) PageToken ¶
func (c *AppsLocationsListCall) PageToken(pageToken string) *AppsLocationsListCall

PageToken sets the optional parameter "pageToken": A page token received from the next_page_token field in the response. Send that page token to receive the subsequent page.

func (*AppsLocationsListCall) Pages ¶
func (c *AppsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AppsLocationsService ¶
type AppsLocationsService struct {
	// contains filtered or unexported fields
}
func NewAppsLocationsService ¶
func NewAppsLocationsService(s *APIService) *AppsLocationsService
func (*AppsLocationsService) Get ¶
func (r *AppsLocationsService) Get(appsId string, locationsId string) *AppsLocationsGetCall

Get: Gets information about a location.

- appsId: Part of `name`. Resource name for the location. - locationsId: Part of `name`. See documentation of `appsId`.

func (*AppsLocationsService) List ¶
func (r *AppsLocationsService) List(appsId string) *AppsLocationsListCall

List: Lists information about the supported locations for this service. This method can be called in two ways: List all public locations: Use the path GET /v1/locations. List project-visible locations: Use the path GET /v1/projects/{project_id}/locations. This may include public locations as well as private or other locations specifically visible to the project.

appsId: Part of `name`. The resource that owns the locations collection, if applicable.
type AppsOperationsGetCall ¶
type AppsOperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*AppsOperationsGetCall) Context ¶
func (c *AppsOperationsGetCall) Context(ctx context.Context) *AppsOperationsGetCall

Context sets the context to be used in this call's Do method.

func (*AppsOperationsGetCall) Do ¶
func (c *AppsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsOperationsGetCall) Fields ¶
func (c *AppsOperationsGetCall) Fields(s ...googleapi.Field) *AppsOperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsOperationsGetCall) Header ¶
func (c *AppsOperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsOperationsGetCall) IfNoneMatch ¶
func (c *AppsOperationsGetCall) IfNoneMatch(entityTag string) *AppsOperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AppsOperationsListCall ¶
type AppsOperationsListCall struct {
	// contains filtered or unexported fields
}
func (*AppsOperationsListCall) Context ¶
func (c *AppsOperationsListCall) Context(ctx context.Context) *AppsOperationsListCall

Context sets the context to be used in this call's Do method.

func (*AppsOperationsListCall) Do ¶
func (c *AppsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)

Do executes the "appengine.apps.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsOperationsListCall) Fields ¶
func (c *AppsOperationsListCall) Fields(s ...googleapi.Field) *AppsOperationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsOperationsListCall) Filter ¶
func (c *AppsOperationsListCall) Filter(filter string) *AppsOperationsListCall

Filter sets the optional parameter "filter": The standard list filter.

func (*AppsOperationsListCall) Header ¶
func (c *AppsOperationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsOperationsListCall) IfNoneMatch ¶
func (c *AppsOperationsListCall) IfNoneMatch(entityTag string) *AppsOperationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsOperationsListCall) PageSize ¶
func (c *AppsOperationsListCall) PageSize(pageSize int64) *AppsOperationsListCall

PageSize sets the optional parameter "pageSize": The standard list page size.

func (*AppsOperationsListCall) PageToken ¶
func (c *AppsOperationsListCall) PageToken(pageToken string) *AppsOperationsListCall

PageToken sets the optional parameter "pageToken": The standard list page token.

func (*AppsOperationsListCall) Pages ¶
func (c *AppsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*AppsOperationsListCall) ReturnPartialSuccess ¶
added in v0.252.0
func (c *AppsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *AppsOperationsListCall

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to true, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field.This can only be true when reading across collections. For example, when parent is set to "projects/example/locations/-".This field is not supported by default and will result in an UNIMPLEMENTED error if set unless explicitly documented otherwise in service or product specific documentation.

type AppsOperationsService ¶
type AppsOperationsService struct {
	// contains filtered or unexported fields
}
func NewAppsOperationsService ¶
func NewAppsOperationsService(s *APIService) *AppsOperationsService
func (*AppsOperationsService) Get ¶
func (r *AppsOperationsService) Get(appsId string, operationsId string) *AppsOperationsGetCall

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- appsId: Part of `name`. The name of the operation resource. - operationsId: Part of `name`. See documentation of `appsId`.

func (*AppsOperationsService) List ¶
func (r *AppsOperationsService) List(appsId string) *AppsOperationsListCall

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.

- appsId: Part of `name`. The name of the operation's parent resource.

type AppsPatchCall ¶
type AppsPatchCall struct {
	// contains filtered or unexported fields
}
func (*AppsPatchCall) Context ¶
func (c *AppsPatchCall) Context(ctx context.Context) *AppsPatchCall

Context sets the context to be used in this call's Do method.

func (*AppsPatchCall) Do ¶
func (c *AppsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsPatchCall) Fields ¶
func (c *AppsPatchCall) Fields(s ...googleapi.Field) *AppsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsPatchCall) Header ¶
func (c *AppsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsPatchCall) UpdateMask ¶
func (c *AppsPatchCall) UpdateMask(updateMask string) *AppsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Standard field mask for the set of fields to be updated.

type AppsRepairCall ¶
type AppsRepairCall struct {
	// contains filtered or unexported fields
}
func (*AppsRepairCall) Context ¶
func (c *AppsRepairCall) Context(ctx context.Context) *AppsRepairCall

Context sets the context to be used in this call's Do method.

func (*AppsRepairCall) Do ¶
func (c *AppsRepairCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.repair" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsRepairCall) Fields ¶
func (c *AppsRepairCall) Fields(s ...googleapi.Field) *AppsRepairCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsRepairCall) Header ¶
func (c *AppsRepairCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsService ¶
type AppsService struct {
	AuthorizedCertificates *AppsAuthorizedCertificatesService

	AuthorizedDomains *AppsAuthorizedDomainsService

	DomainMappings *AppsDomainMappingsService

	Firewall *AppsFirewallService

	Locations *AppsLocationsService

	Operations *AppsOperationsService

	Services *AppsServicesService
	// contains filtered or unexported fields
}
func NewAppsService ¶
func NewAppsService(s *APIService) *AppsService
func (*AppsService) Create ¶
func (r *AppsService) Create(application *Application) *AppsCreateCall

Create: Creates an App Engine application for a Google Cloud Platform project. Required fields: id - The ID of the target Cloud Platform project. location - The region (https://cloud.google.com/appengine/docs/locations) where you want the App Engine application located.For more information about App Engine applications, see Managing Projects, Applications, and Billing (https://cloud.google.com/appengine/docs/standard/python/console/).

func (*AppsService) Get ¶
func (r *AppsService) Get(appsId string) *AppsGetCall

Get: Gets information about an application.

appsId: Part of `name`. Name of the Application resource to get. Example: apps/myapp.
func (*AppsService) ListRuntimes ¶
added in v0.148.0
func (r *AppsService) ListRuntimes(appsId string) *AppsListRuntimesCall

ListRuntimes: Lists all the available runtimes for the application.

appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
func (*AppsService) Patch ¶
func (r *AppsService) Patch(appsId string, application *Application) *AppsPatchCall

Patch: Updates the specified Application resource. You can update the following fields: auth_domain - Google authentication domain for controlling user access to the application. default_cookie_expiration - Cookie expiration policy for the application. iap - Identity-Aware Proxy properties for the application.

appsId: Part of `name`. Name of the Application resource to update. Example: apps/myapp.
func (*AppsService) Repair ¶
func (r *AppsService) Repair(appsId string, repairapplicationrequest *RepairApplicationRequest) *AppsRepairCall

Repair: Recreates the required App Engine features for the specified App Engine application, for example a Cloud Storage bucket or App Engine service account. Use this method if you receive an error message about a missing feature, for example, Error retrieving the App Engine service account. If you have deleted your App Engine service account, this will not be able to recreate it. Instead, you should attempt to use the IAM undelete API if possible at https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts/undelete?apix_params=%7B"name"%3A"projects%2F-%2FserviceAccounts%2Funique_id"%2C"resource"%3A%7B%7D%7D . If the deletion was recent, the numeric ID can be found in the Cloud Console Activity Log.

appsId: Part of `name`. Name of the application to repair. Example: apps/myapp.
type AppsServicesDeleteCall ¶
type AppsServicesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesDeleteCall) Context ¶
func (c *AppsServicesDeleteCall) Context(ctx context.Context) *AppsServicesDeleteCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesDeleteCall) Do ¶
func (c *AppsServicesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.services.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesDeleteCall) Fields ¶
func (c *AppsServicesDeleteCall) Fields(s ...googleapi.Field) *AppsServicesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesDeleteCall) Header ¶
func (c *AppsServicesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsServicesGetCall ¶
type AppsServicesGetCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesGetCall) Context ¶
func (c *AppsServicesGetCall) Context(ctx context.Context) *AppsServicesGetCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesGetCall) Do ¶
func (c *AppsServicesGetCall) Do(opts ...googleapi.CallOption) (*Service, error)

Do executes the "appengine.apps.services.get" call. Any non-2xx status code is an error. Response headers are in either *Service.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesGetCall) Fields ¶
func (c *AppsServicesGetCall) Fields(s ...googleapi.Field) *AppsServicesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesGetCall) Header ¶
func (c *AppsServicesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsServicesGetCall) IfNoneMatch ¶
func (c *AppsServicesGetCall) IfNoneMatch(entityTag string) *AppsServicesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsServicesGetCall) IncludeExtraData ¶
added in v0.142.0
func (c *AppsServicesGetCall) IncludeExtraData(includeExtraData string) *AppsServicesGetCall

IncludeExtraData sets the optional parameter "includeExtraData": Options to include extra data

Possible values:

"INCLUDE_EXTRA_DATA_UNSPECIFIED" - Unspecified: No extra data will be


returned

"INCLUDE_EXTRA_DATA_NONE" - Do not return any extra data
"INCLUDE_GOOGLE_GENERATED_METADATA" - Return GGCM associated with the


resources

type AppsServicesListCall ¶
type AppsServicesListCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesListCall) Context ¶
func (c *AppsServicesListCall) Context(ctx context.Context) *AppsServicesListCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesListCall) Do ¶
func (c *AppsServicesListCall) Do(opts ...googleapi.CallOption) (*ListServicesResponse, error)

Do executes the "appengine.apps.services.list" call. Any non-2xx status code is an error. Response headers are in either *ListServicesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesListCall) Fields ¶
func (c *AppsServicesListCall) Fields(s ...googleapi.Field) *AppsServicesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesListCall) Header ¶
func (c *AppsServicesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsServicesListCall) IfNoneMatch ¶
func (c *AppsServicesListCall) IfNoneMatch(entityTag string) *AppsServicesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsServicesListCall) PageSize ¶
func (c *AppsServicesListCall) PageSize(pageSize int64) *AppsServicesListCall

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

func (*AppsServicesListCall) PageToken ¶
func (c *AppsServicesListCall) PageToken(pageToken string) *AppsServicesListCall

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

func (*AppsServicesListCall) Pages ¶
func (c *AppsServicesListCall) Pages(ctx context.Context, f func(*ListServicesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AppsServicesPatchCall ¶
type AppsServicesPatchCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesPatchCall) Context ¶
func (c *AppsServicesPatchCall) Context(ctx context.Context) *AppsServicesPatchCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesPatchCall) Do ¶
func (c *AppsServicesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.services.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesPatchCall) Fields ¶
func (c *AppsServicesPatchCall) Fields(s ...googleapi.Field) *AppsServicesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesPatchCall) Header ¶
func (c *AppsServicesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsServicesPatchCall) MigrateTraffic ¶
func (c *AppsServicesPatchCall) MigrateTraffic(migrateTraffic bool) *AppsServicesPatchCall

MigrateTraffic sets the optional parameter "migrateTraffic": Set to true to gradually shift traffic to one or more versions that you specify. By default, traffic is shifted immediately. For gradual traffic migration, the target versions must be located within instances that are configured for both warmup requests (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#InboundServiceType) and automatic scaling (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#AutomaticScaling). You must specify the shardBy (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services#ShardBy) field in the Service resource. Gradual traffic migration is not supported in the App Engine flexible environment. For examples, see Migrating and Splitting Traffic (https://cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic).

func (*AppsServicesPatchCall) UpdateMask ¶
func (c *AppsServicesPatchCall) UpdateMask(updateMask string) *AppsServicesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Standard field mask for the set of fields to be updated.

type AppsServicesService ¶
type AppsServicesService struct {
	Versions *AppsServicesVersionsService
	// contains filtered or unexported fields
}
func NewAppsServicesService ¶
func NewAppsServicesService(s *APIService) *AppsServicesService
func (*AppsServicesService) Delete ¶
func (r *AppsServicesService) Delete(appsId string, servicesId string) *AppsServicesDeleteCall

Delete: Deletes the specified service and all enclosed versions.

appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default.
servicesId: Part of `name`. See documentation of `appsId`.
func (*AppsServicesService) Get ¶
func (r *AppsServicesService) Get(appsId string, servicesId string) *AppsServicesGetCall

Get: Gets the current configuration of the specified service.

appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default.
servicesId: Part of `name`. See documentation of `appsId`.
func (*AppsServicesService) List ¶
func (r *AppsServicesService) List(appsId string) *AppsServicesListCall

List: Lists all the services in the application.

appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
func (*AppsServicesService) Patch ¶
func (r *AppsServicesService) Patch(appsId string, servicesId string, service *Service) *AppsServicesPatchCall

Patch: Updates the configuration of the specified service.

appsId: Part of `name`. Name of the resource to update. Example: apps/myapp/services/default.
servicesId: Part of `name`. See documentation of `appsId`.
type AppsServicesVersionsCreateCall ¶
type AppsServicesVersionsCreateCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesVersionsCreateCall) Context ¶
func (c *AppsServicesVersionsCreateCall) Context(ctx context.Context) *AppsServicesVersionsCreateCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesVersionsCreateCall) Do ¶
func (c *AppsServicesVersionsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.services.versions.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesVersionsCreateCall) Fields ¶
func (c *AppsServicesVersionsCreateCall) Fields(s ...googleapi.Field) *AppsServicesVersionsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesVersionsCreateCall) Header ¶
func (c *AppsServicesVersionsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsServicesVersionsDeleteCall ¶
type AppsServicesVersionsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesVersionsDeleteCall) Context ¶
func (c *AppsServicesVersionsDeleteCall) Context(ctx context.Context) *AppsServicesVersionsDeleteCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesVersionsDeleteCall) Do ¶
func (c *AppsServicesVersionsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.services.versions.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesVersionsDeleteCall) Fields ¶
func (c *AppsServicesVersionsDeleteCall) Fields(s ...googleapi.Field) *AppsServicesVersionsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesVersionsDeleteCall) Header ¶
func (c *AppsServicesVersionsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsServicesVersionsGetCall ¶
type AppsServicesVersionsGetCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesVersionsGetCall) Context ¶
func (c *AppsServicesVersionsGetCall) Context(ctx context.Context) *AppsServicesVersionsGetCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesVersionsGetCall) Do ¶
func (c *AppsServicesVersionsGetCall) Do(opts ...googleapi.CallOption) (*Version, error)

Do executes the "appengine.apps.services.versions.get" call. Any non-2xx status code is an error. Response headers are in either *Version.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesVersionsGetCall) Fields ¶
func (c *AppsServicesVersionsGetCall) Fields(s ...googleapi.Field) *AppsServicesVersionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesVersionsGetCall) Header ¶
func (c *AppsServicesVersionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsServicesVersionsGetCall) IfNoneMatch ¶
func (c *AppsServicesVersionsGetCall) IfNoneMatch(entityTag string) *AppsServicesVersionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsServicesVersionsGetCall) IncludeExtraData ¶
added in v0.142.0
func (c *AppsServicesVersionsGetCall) IncludeExtraData(includeExtraData string) *AppsServicesVersionsGetCall

IncludeExtraData sets the optional parameter "includeExtraData": Options to include extra data

Possible values:

"INCLUDE_EXTRA_DATA_UNSPECIFIED" - Unspecified: No extra data will be


returned

"INCLUDE_EXTRA_DATA_NONE" - Do not return any extra data
"INCLUDE_GOOGLE_GENERATED_METADATA" - Return GGCM associated with the


resources

func (*AppsServicesVersionsGetCall) View ¶
func (c *AppsServicesVersionsGetCall) View(view string) *AppsServicesVersionsGetCall

View sets the optional parameter "view": Controls the set of fields returned in the Get response.

Possible values:

"BASIC" - Basic version information including scaling and inbound


services, but not detailed deployment information.

"FULL" - The information from BASIC, plus detailed information about the


deployment. This format is required when creating resources, but is not returned in Get or List by default.

type AppsServicesVersionsInstancesDebugCall ¶
type AppsServicesVersionsInstancesDebugCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesVersionsInstancesDebugCall) Context ¶
func (c *AppsServicesVersionsInstancesDebugCall) Context(ctx context.Context) *AppsServicesVersionsInstancesDebugCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesVersionsInstancesDebugCall) Do ¶
func (c *AppsServicesVersionsInstancesDebugCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.services.versions.instances.debug" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesVersionsInstancesDebugCall) Fields ¶
func (c *AppsServicesVersionsInstancesDebugCall) Fields(s ...googleapi.Field) *AppsServicesVersionsInstancesDebugCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesVersionsInstancesDebugCall) Header ¶
func (c *AppsServicesVersionsInstancesDebugCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsServicesVersionsInstancesDeleteCall ¶
type AppsServicesVersionsInstancesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesVersionsInstancesDeleteCall) Context ¶
func (c *AppsServicesVersionsInstancesDeleteCall) Context(ctx context.Context) *AppsServicesVersionsInstancesDeleteCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesVersionsInstancesDeleteCall) Do ¶
func (c *AppsServicesVersionsInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.services.versions.instances.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesVersionsInstancesDeleteCall) Fields ¶
func (c *AppsServicesVersionsInstancesDeleteCall) Fields(s ...googleapi.Field) *AppsServicesVersionsInstancesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesVersionsInstancesDeleteCall) Header ¶
func (c *AppsServicesVersionsInstancesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsServicesVersionsInstancesGetCall ¶
type AppsServicesVersionsInstancesGetCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesVersionsInstancesGetCall) Context ¶
func (c *AppsServicesVersionsInstancesGetCall) Context(ctx context.Context) *AppsServicesVersionsInstancesGetCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesVersionsInstancesGetCall) Do ¶
func (c *AppsServicesVersionsInstancesGetCall) Do(opts ...googleapi.CallOption) (*Instance, error)

Do executes the "appengine.apps.services.versions.instances.get" call. Any non-2xx status code is an error. Response headers are in either *Instance.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesVersionsInstancesGetCall) Fields ¶
func (c *AppsServicesVersionsInstancesGetCall) Fields(s ...googleapi.Field) *AppsServicesVersionsInstancesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesVersionsInstancesGetCall) Header ¶
func (c *AppsServicesVersionsInstancesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsServicesVersionsInstancesGetCall) IfNoneMatch ¶
func (c *AppsServicesVersionsInstancesGetCall) IfNoneMatch(entityTag string) *AppsServicesVersionsInstancesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AppsServicesVersionsInstancesListCall ¶
type AppsServicesVersionsInstancesListCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesVersionsInstancesListCall) Context ¶
func (c *AppsServicesVersionsInstancesListCall) Context(ctx context.Context) *AppsServicesVersionsInstancesListCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesVersionsInstancesListCall) Do ¶
func (c *AppsServicesVersionsInstancesListCall) Do(opts ...googleapi.CallOption) (*ListInstancesResponse, error)

Do executes the "appengine.apps.services.versions.instances.list" call. Any non-2xx status code is an error. Response headers are in either *ListInstancesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesVersionsInstancesListCall) Fields ¶
func (c *AppsServicesVersionsInstancesListCall) Fields(s ...googleapi.Field) *AppsServicesVersionsInstancesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesVersionsInstancesListCall) Header ¶
func (c *AppsServicesVersionsInstancesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsServicesVersionsInstancesListCall) IfNoneMatch ¶
func (c *AppsServicesVersionsInstancesListCall) IfNoneMatch(entityTag string) *AppsServicesVersionsInstancesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsServicesVersionsInstancesListCall) PageSize ¶
func (c *AppsServicesVersionsInstancesListCall) PageSize(pageSize int64) *AppsServicesVersionsInstancesListCall

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

func (*AppsServicesVersionsInstancesListCall) PageToken ¶
func (c *AppsServicesVersionsInstancesListCall) PageToken(pageToken string) *AppsServicesVersionsInstancesListCall

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

func (*AppsServicesVersionsInstancesListCall) Pages ¶
func (c *AppsServicesVersionsInstancesListCall) Pages(ctx context.Context, f func(*ListInstancesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AppsServicesVersionsInstancesService ¶
type AppsServicesVersionsInstancesService struct {
	// contains filtered or unexported fields
}
func NewAppsServicesVersionsInstancesService ¶
func NewAppsServicesVersionsInstancesService(s *APIService) *AppsServicesVersionsInstancesService
func (*AppsServicesVersionsInstancesService) Debug ¶
func (r *AppsServicesVersionsInstancesService) Debug(appsId string, servicesId string, versionsId string, instancesId string, debuginstancerequest *DebugInstanceRequest) *AppsServicesVersionsInstancesDebugCall

Debug: Enables debugging on a VM instance. This allows you to use the SSH command to connect to the virtual machine where the instance lives. While in "debug mode", the instance continues to serve live traffic. You should delete the instance when you are done debugging and then allow the system to take over and determine if another instance should be started.Only applicable for instances in App Engine flexible environment.

appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default/versions/v1/instances/instance-1.
instancesId: Part of `name`. See documentation of `appsId`.
servicesId: Part of `name`. See documentation of `appsId`.
versionsId: Part of `name`. See documentation of `appsId`.
func (*AppsServicesVersionsInstancesService) Delete ¶
func (r *AppsServicesVersionsInstancesService) Delete(appsId string, servicesId string, versionsId string, instancesId string) *AppsServicesVersionsInstancesDeleteCall

Delete: Stops a running instance.The instance might be automatically recreated based on the scaling settings of the version. For more information, see "How Instances are Managed" (standard environment (https://cloud.google.com/appengine/docs/standard/python/how-instances-are-managed) | flexible environment (https://cloud.google.com/appengine/docs/flexible/python/how-instances-are-managed)).To ensure that instances are not re-created and avoid getting billed, you can stop all instances within the target version by changing the serving status of the version to STOPPED with the apps.services.versions.patch (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/patch) method.

appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default/versions/v1/instances/instance-1.
instancesId: Part of `name`. See documentation of `appsId`.
servicesId: Part of `name`. See documentation of `appsId`.
versionsId: Part of `name`. See documentation of `appsId`.
func (*AppsServicesVersionsInstancesService) Get ¶
func (r *AppsServicesVersionsInstancesService) Get(appsId string, servicesId string, versionsId string, instancesId string) *AppsServicesVersionsInstancesGetCall

Get: Gets instance information.

appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default/versions/v1/instances/instance-1.
instancesId: Part of `name`. See documentation of `appsId`.
servicesId: Part of `name`. See documentation of `appsId`.
versionsId: Part of `name`. See documentation of `appsId`.
func (*AppsServicesVersionsInstancesService) List ¶
func (r *AppsServicesVersionsInstancesService) List(appsId string, servicesId string, versionsId string) *AppsServicesVersionsInstancesListCall

List: Lists the instances of a version.Tip: To aggregate details about instances over time, see the Stackdriver Monitoring API (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list).

appsId: Part of `parent`. Name of the parent Version resource. Example: apps/myapp/services/default/versions/v1.
servicesId: Part of `parent`. See documentation of `appsId`.
versionsId: Part of `parent`. See documentation of `appsId`.
type AppsServicesVersionsListCall ¶
type AppsServicesVersionsListCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesVersionsListCall) Context ¶
func (c *AppsServicesVersionsListCall) Context(ctx context.Context) *AppsServicesVersionsListCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesVersionsListCall) Do ¶
func (c *AppsServicesVersionsListCall) Do(opts ...googleapi.CallOption) (*ListVersionsResponse, error)

Do executes the "appengine.apps.services.versions.list" call. Any non-2xx status code is an error. Response headers are in either *ListVersionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesVersionsListCall) Fields ¶
func (c *AppsServicesVersionsListCall) Fields(s ...googleapi.Field) *AppsServicesVersionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesVersionsListCall) Header ¶
func (c *AppsServicesVersionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsServicesVersionsListCall) IfNoneMatch ¶
func (c *AppsServicesVersionsListCall) IfNoneMatch(entityTag string) *AppsServicesVersionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AppsServicesVersionsListCall) PageSize ¶
func (c *AppsServicesVersionsListCall) PageSize(pageSize int64) *AppsServicesVersionsListCall

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

func (*AppsServicesVersionsListCall) PageToken ¶
func (c *AppsServicesVersionsListCall) PageToken(pageToken string) *AppsServicesVersionsListCall

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

func (*AppsServicesVersionsListCall) Pages ¶
func (c *AppsServicesVersionsListCall) Pages(ctx context.Context, f func(*ListVersionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*AppsServicesVersionsListCall) View ¶
func (c *AppsServicesVersionsListCall) View(view string) *AppsServicesVersionsListCall

View sets the optional parameter "view": Controls the set of fields returned in the List response.

Possible values:

"BASIC" - Basic version information including scaling and inbound


services, but not detailed deployment information.

"FULL" - The information from BASIC, plus detailed information about the


deployment. This format is required when creating resources, but is not returned in Get or List by default.

type AppsServicesVersionsPatchCall ¶
type AppsServicesVersionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*AppsServicesVersionsPatchCall) Context ¶
func (c *AppsServicesVersionsPatchCall) Context(ctx context.Context) *AppsServicesVersionsPatchCall

Context sets the context to be used in this call's Do method.

func (*AppsServicesVersionsPatchCall) Do ¶
func (c *AppsServicesVersionsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.apps.services.versions.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AppsServicesVersionsPatchCall) Fields ¶
func (c *AppsServicesVersionsPatchCall) Fields(s ...googleapi.Field) *AppsServicesVersionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AppsServicesVersionsPatchCall) Header ¶
func (c *AppsServicesVersionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AppsServicesVersionsPatchCall) UpdateMask ¶
func (c *AppsServicesVersionsPatchCall) UpdateMask(updateMask string) *AppsServicesVersionsPatchCall

UpdateMask sets the optional parameter "updateMask": Standard field mask for the set of fields to be updated.

type AppsServicesVersionsService ¶
type AppsServicesVersionsService struct {
	Instances *AppsServicesVersionsInstancesService
	// contains filtered or unexported fields
}
func NewAppsServicesVersionsService ¶
func NewAppsServicesVersionsService(s *APIService) *AppsServicesVersionsService
func (*AppsServicesVersionsService) Create ¶
func (r *AppsServicesVersionsService) Create(appsId string, servicesId string, version *Version) *AppsServicesVersionsCreateCall

Create: Deploys code and resource files to a new version.

appsId: Part of `parent`. Name of the parent resource to create this version under. Example: apps/myapp/services/default.
servicesId: Part of `parent`. See documentation of `appsId`.
func (*AppsServicesVersionsService) Delete ¶
func (r *AppsServicesVersionsService) Delete(appsId string, servicesId string, versionsId string) *AppsServicesVersionsDeleteCall

Delete: Deletes an existing Version resource.

appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default/versions/v1.
servicesId: Part of `name`. See documentation of `appsId`.
versionsId: Part of `name`. See documentation of `appsId`.
func (*AppsServicesVersionsService) Get ¶
func (r *AppsServicesVersionsService) Get(appsId string, servicesId string, versionsId string) *AppsServicesVersionsGetCall

Get: Gets the specified Version resource. By default, only a BASIC_VIEW will be returned. Specify the FULL_VIEW parameter to get the full resource.

appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default/versions/v1.
servicesId: Part of `name`. See documentation of `appsId`.
versionsId: Part of `name`. See documentation of `appsId`.
func (*AppsServicesVersionsService) List ¶
func (r *AppsServicesVersionsService) List(appsId string, servicesId string) *AppsServicesVersionsListCall

List: Lists the versions of a service.

appsId: Part of `parent`. Name of the parent Service resource. Example: apps/myapp/services/default.
servicesId: Part of `parent`. See documentation of `appsId`.
func (*AppsServicesVersionsService) Patch ¶
func (r *AppsServicesVersionsService) Patch(appsId string, servicesId string, versionsId string, version *Version) *AppsServicesVersionsPatchCall

Patch: Updates the specified Version resource. You can specify the following fields depending on the App Engine environment and type of scaling that the version resource uses:Standard environment instance_class (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.instance_class)automatic scaling in the standard environment: automatic_scaling.min_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.max_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling) automaticScaling.standard_scheduler_settings.max_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.min_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.target_cpu_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.target_throughput_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#StandardSchedulerSettings)basic scaling or manual scaling in the standard environment: serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.serving_status) manual_scaling.instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#manualscaling)Flexible environment serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.serving_status)automatic scaling in the flexible environment: automatic_scaling.min_total_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.max_total_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.cool_down_period_sec (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.cpu_utilization.target_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling)manual scaling in the flexible environment: manual_scaling.instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#manualscaling)

appsId: Part of `name`. Name of the resource to update. Example: apps/myapp/services/default/versions/1.
servicesId: Part of `name`. See documentation of `appsId`.
versionsId: Part of `name`. See documentation of `appsId`.
type AuthorizedCertificate ¶
type AuthorizedCertificate struct {
	// CertificateRawData: The SSL certificate serving the AuthorizedCertificate
	// resource. This must be obtained independently from a certificate authority.
	CertificateRawData *CertificateRawData `json:"certificateRawData,omitempty"`
	// DisplayName: The user-specified display name of the certificate. This is not
	// guaranteed to be unique. Example: My Certificate.
	DisplayName string `json:"displayName,omitempty"`
	// DomainMappingsCount: Aggregate count of the domain mappings with this
	// certificate mapped. This count includes domain mappings on applications for
	// which the user does not have VIEWER permissions.Only returned by GET or LIST
	// requests when specifically requested by the view=FULL_CERTIFICATE
	// option.@OutputOnly
	DomainMappingsCount int64 `json:"domainMappingsCount,omitempty"`
	// DomainNames: Output only. Topmost applicable domains of this certificate.
	// This certificate applies to these domains and their subdomains. Example:
	// example.com.@OutputOnly
	DomainNames []string `json:"domainNames,omitempty"`
	// ExpireTime: The time when this certificate expires. To update the renewal
	// time on this certificate, upload an SSL certificate with a different
	// expiration time using
	// AuthorizedCertificates.UpdateAuthorizedCertificate.@OutputOnly
	ExpireTime string `json:"expireTime,omitempty"`
	// Id: Output only. Relative name of the certificate. This is a unique value
	// autogenerated on AuthorizedCertificate resource creation. Example:
	// 12345.@OutputOnly
	Id string `json:"id,omitempty"`
	// ManagedCertificate: Only applicable if this certificate is managed by App
	// Engine. Managed certificates are tied to the lifecycle of a DomainMapping
	// and cannot be updated or deleted via the AuthorizedCertificates API. If this
	// certificate is manually administered by the user, this field will be
	// empty.@OutputOnly
	ManagedCertificate *ManagedCertificate `json:"managedCertificate,omitempty"`
	// Name: Output only. Full path to the AuthorizedCertificate resource in the
	// API. Example: apps/myapp/authorizedCertificates/12345.@OutputOnly
	Name string `json:"name,omitempty"`
	// VisibleDomainMappings: Output only. The full paths to user visible Domain
	// Mapping resources that have this certificate mapped. Example:
	// apps/myapp/domainMappings/example.com.This may not represent the full list
	// of mapped domain mappings if the user does not have VIEWER permissions on
	// all of the applications that have this certificate mapped. See
	// domain_mappings_count for a complete count.Only returned by GET or LIST
	// requests when specifically requested by the view=FULL_CERTIFICATE
	// option.@OutputOnly
	VisibleDomainMappings []string `json:"visibleDomainMappings,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CertificateRawData") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CertificateRawData") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuthorizedCertificate: An SSL certificate that a user has been authorized to administer. A user is authorized to administer any certificate that applies to one of their authorized domains.

func (AuthorizedCertificate) MarshalJSON ¶
func (s AuthorizedCertificate) MarshalJSON() ([]byte, error)
type AuthorizedDomain ¶
type AuthorizedDomain struct {
	// Id: Fully qualified domain name of the domain authorized for use. Example:
	// example.com.
	Id string `json:"id,omitempty"`
	// Name: Full path to the AuthorizedDomain resource in the API. Example:
	// apps/myapp/authorizedDomains/example.com.@OutputOnly
	Name string `json:"name,omitempty"`
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

AuthorizedDomain: A domain that a user has been authorized to administer. To authorize use of a domain, verify ownership via Search Console (https://search.google.com/search-console/welcome).

func (AuthorizedDomain) MarshalJSON ¶
func (s AuthorizedDomain) MarshalJSON() ([]byte, error)
type AutomaticScaling ¶
type AutomaticScaling struct {
	// CoolDownPeriod: The time period that the Autoscaler
	// (https://cloud.google.com/compute/docs/autoscaler/) should wait before it
	// starts collecting information from a new instance. This prevents the
	// autoscaler from collecting information when the instance is initializing,
	// during which the collected usage would not be reliable. Only applicable in
	// the App Engine flexible environment.
	CoolDownPeriod string `json:"coolDownPeriod,omitempty"`
	// CpuUtilization: Target scaling by CPU usage.
	CpuUtilization *CpuUtilization `json:"cpuUtilization,omitempty"`
	// CustomMetrics: Target scaling by user-provided metrics. Only applicable in
	// the App Engine flexible environment.
	CustomMetrics []*CustomMetric `json:"customMetrics,omitempty"`
	// DiskUtilization: Target scaling by disk usage.
	DiskUtilization *DiskUtilization `json:"diskUtilization,omitempty"`
	// MaxConcurrentRequests: Number of concurrent requests an automatic scaling
	// instance can accept before the scheduler spawns a new instance.Defaults to a
	// runtime-specific value.
	MaxConcurrentRequests int64 `json:"maxConcurrentRequests,omitempty"`
	// MaxIdleInstances: Maximum number of idle instances that should be maintained
	// for this version.
	MaxIdleInstances int64 `json:"maxIdleInstances,omitempty"`
	// MaxPendingLatency: Maximum amount of time that a request should wait in the
	// pending queue before starting a new instance to handle it.
	MaxPendingLatency string `json:"maxPendingLatency,omitempty"`
	// MaxTotalInstances: Maximum number of instances that should be started to
	// handle requests for this version.
	MaxTotalInstances int64 `json:"maxTotalInstances,omitempty"`
	// MinIdleInstances: Minimum number of idle instances that should be maintained
	// for this version. Only applicable for the default version of a service.
	MinIdleInstances int64 `json:"minIdleInstances,omitempty"`
	// MinPendingLatency: Minimum amount of time a request should wait in the
	// pending queue before starting a new instance to handle it.
	MinPendingLatency string `json:"minPendingLatency,omitempty"`
	// MinTotalInstances: Minimum number of running instances that should be
	// maintained for this version.
	MinTotalInstances int64 `json:"minTotalInstances,omitempty"`
	// NetworkUtilization: Target scaling by network usage.
	NetworkUtilization *NetworkUtilization `json:"networkUtilization,omitempty"`
	// RequestUtilization: Target scaling by request utilization.
	RequestUtilization *RequestUtilization `json:"requestUtilization,omitempty"`
	// StandardSchedulerSettings: Scheduler settings for standard environment.
	StandardSchedulerSettings *StandardSchedulerSettings `json:"standardSchedulerSettings,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CoolDownPeriod") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CoolDownPeriod") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AutomaticScaling: Automatic scaling is based on request rate, response latencies, and other application metrics.

func (AutomaticScaling) MarshalJSON ¶
func (s AutomaticScaling) MarshalJSON() ([]byte, error)
type BasicScaling ¶
type BasicScaling struct {
	// IdleTimeout: Duration of time after the last request that an instance must
	// wait before the instance is shut down.
	IdleTimeout string `json:"idleTimeout,omitempty"`
	// MaxInstances: Maximum number of instances to create for this version.
	MaxInstances int64 `json:"maxInstances,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IdleTimeout") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IdleTimeout") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BasicScaling: A service with basic scaling will create an instance when the application receives a request. The instance will be turned down when the app becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity.

func (BasicScaling) MarshalJSON ¶
func (s BasicScaling) MarshalJSON() ([]byte, error)
type BatchUpdateIngressRulesRequest ¶
type BatchUpdateIngressRulesRequest struct {
	// IngressRules: A list of FirewallRules to replace the existing set.
	IngressRules []*FirewallRule `json:"ingressRules,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IngressRules") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IngressRules") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdateIngressRulesRequest: Request message for Firewall.BatchUpdateIngressRules.

func (BatchUpdateIngressRulesRequest) MarshalJSON ¶
func (s BatchUpdateIngressRulesRequest) MarshalJSON() ([]byte, error)
type BatchUpdateIngressRulesResponse ¶
type BatchUpdateIngressRulesResponse struct {
	// IngressRules: The full list of ingress FirewallRules for this application.
	IngressRules []*FirewallRule `json:"ingressRules,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "IngressRules") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IngressRules") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdateIngressRulesResponse: Response message for Firewall.UpdateAllIngressRules.

func (BatchUpdateIngressRulesResponse) MarshalJSON ¶
func (s BatchUpdateIngressRulesResponse) MarshalJSON() ([]byte, error)
type BuildInfo ¶
type BuildInfo struct {
	// CloudBuildId: The Google Cloud Build id. Example:
	// "f966068f-08b2-42c8-bdfe-74137dff2bf9"
	CloudBuildId string `json:"cloudBuildId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CloudBuildId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CloudBuildId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BuildInfo: Google Cloud Build information.

func (BuildInfo) MarshalJSON ¶
func (s BuildInfo) MarshalJSON() ([]byte, error)
type CertificateRawData ¶
type CertificateRawData struct {
	// PrivateKey: Unencrypted PEM encoded RSA private key. This field is set once
	// on certificate creation and then encrypted. The key size must be 2048 bits
	// or fewer. Must include the header and footer. Example: -----BEGIN RSA
	// PRIVATE KEY----- -----END RSA PRIVATE KEY----- @InputOnly
	PrivateKey string `json:"privateKey,omitempty"`
	// PublicCertificate: PEM encoded x.509 public key certificate. This field is
	// set once on certificate creation. Must include the header and footer.
	// Example: -----BEGIN CERTIFICATE----- -----END CERTIFICATE-----
	PublicCertificate string `json:"publicCertificate,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PrivateKey") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PrivateKey") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CertificateRawData: An SSL certificate obtained from a certificate authority.

func (CertificateRawData) MarshalJSON ¶
func (s CertificateRawData) MarshalJSON() ([]byte, error)
type CloudBuildOptions ¶
type CloudBuildOptions struct {
	// AppYamlPath: Path to the yaml file used in deployment, used to determine
	// runtime configuration details.Required for flexible environment builds.See
	// https://cloud.google.com/appengine/docs/standard/python/config/appref for
	// more details.
	AppYamlPath string `json:"appYamlPath,omitempty"`
	// CloudBuildTimeout: The Cloud Build timeout used as part of any dependent
	// builds performed by version creation. Defaults to 10 minutes.
	CloudBuildTimeout string `json:"cloudBuildTimeout,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AppYamlPath") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppYamlPath") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CloudBuildOptions: Options for the build operations performed as a part of the version deployment. Only applicable for App Engine flexible environment when creating a version using source code directly.

func (CloudBuildOptions) MarshalJSON ¶
func (s CloudBuildOptions) MarshalJSON() ([]byte, error)
type ContainerInfo ¶
type ContainerInfo struct {
	// Image: URI to the hosted container image in Google Container Registry. The
	// URI must be fully qualified and include a tag or digest. Examples:
	// "gcr.io/my-project/image:tag" or "gcr.io/my-project/image@digest"
	Image string `json:"image,omitempty"`
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

ContainerInfo: Docker image that is used to create a container and start a VM instance for the version that you deploy. Only applicable for instances running in the App Engine flexible environment.

func (ContainerInfo) MarshalJSON ¶
func (s ContainerInfo) MarshalJSON() ([]byte, error)
type ContainerState ¶
added in v0.148.0
type ContainerState struct {
	CurrentReasons *Reasons `json:"currentReasons,omitempty"`
	// PreviousReasons: The previous and current reasons for a container state will
	// be sent for a container event. CLHs that need to know the signal that caused
	// the container event to trigger (edges) as opposed to just knowing the state
	// can act upon differences in the previous and current reasons.Reasons will be
	// provided for every system: service management, data governance, abuse, and
	// billing.If this is a CCFE-triggered event used for reconciliation then the
	// current reasons will be set to their *_CONTROL_PLANE_SYNC state. The
	// previous reasons will contain the last known set of non-unknown
	// non-control_plane_sync reasons for the state.
	PreviousReasons *Reasons `json:"previousReasons,omitempty"`
	// State: The current state of the container. This state is the culmination of
	// all of the opinions from external systems that CCFE knows about of the
	// container.
	//
	// Possible values:
	//   "UNKNOWN_STATE" - A container should never be in an unknown state. Receipt
	// of a container with this state is an error.
	//   "ON" - CCFE considers the container to be serving or transitioning into
	// serving.
	//   "OFF" - CCFE considers the container to be in an OFF state. This could
	// occur due to various factors. The state could be triggered by
	// Google-internal audits (ex. abuse suspension, billing closed) or cleanups
	// trigged by compliance systems (ex. data governance hide). User-initiated
	// events such as service management deactivation trigger a container to an OFF
	// state.CLHs might choose to do nothing in this case or to turn off costly
	// resources. CLHs need to consider the customer experience if an ON/OFF/ON
	// sequence of state transitions occurs vs. the cost of deleting resources,
	// keeping metadata about resources, or even keeping resources live for a
	// period of time.CCFE will not send any new customer requests to the CLH when
	// the container is in an OFF state. However, CCFE will allow all previous
	// customer requests relayed to CLH to complete.
	//   "DELETED" - This state indicates that the container has been (or is being)
	// completely removed. This is often due to a data governance purge request and
	// therefore resources should be deleted when this state is reached.
	State string `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CurrentReasons") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurrentReasons") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ContainerState: ContainerState contains the externally-visible container state that is used to communicate the state and reasoning for that state to the CLH. This data is not persisted by CCFE, but is instead derived from CCFE's internal representation of the container state.

func (ContainerState) MarshalJSON ¶
added in v0.148.0
func (s ContainerState) MarshalJSON() ([]byte, error)
type CpuUtilization ¶
type CpuUtilization struct {
	// AggregationWindowLength: Period of time over which CPU utilization is
	// calculated.
	AggregationWindowLength string `json:"aggregationWindowLength,omitempty"`
	// TargetUtilization: Target CPU utilization ratio to maintain when scaling.
	// Must be between 0 and 1.
	TargetUtilization float64 `json:"targetUtilization,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AggregationWindowLength") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AggregationWindowLength") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CpuUtilization: Target scaling by CPU usage.

func (CpuUtilization) MarshalJSON ¶
func (s CpuUtilization) MarshalJSON() ([]byte, error)
func (*CpuUtilization) UnmarshalJSON ¶
func (s *CpuUtilization) UnmarshalJSON(data []byte) error
type CreateVersionMetadataV1 ¶
type CreateVersionMetadataV1 struct {
	// CloudBuildId: The Cloud Build ID if one was created as part of the version
	// create. @OutputOnly
	CloudBuildId string `json:"cloudBuildId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CloudBuildId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CloudBuildId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateVersionMetadataV1: Metadata for the given google.longrunning.Operation during a google.appengine.v1.CreateVersionRequest.

func (CreateVersionMetadataV1) MarshalJSON ¶
func (s CreateVersionMetadataV1) MarshalJSON() ([]byte, error)
type CreateVersionMetadataV1Alpha ¶
type CreateVersionMetadataV1Alpha struct {
	// CloudBuildId: The Cloud Build ID if one was created as part of the version
	// create. @OutputOnly
	CloudBuildId string `json:"cloudBuildId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CloudBuildId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CloudBuildId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateVersionMetadataV1Alpha: Metadata for the given google.longrunning.Operation during a google.appengine.v1alpha.CreateVersionRequest.

func (CreateVersionMetadataV1Alpha) MarshalJSON ¶
func (s CreateVersionMetadataV1Alpha) MarshalJSON() ([]byte, error)
type CreateVersionMetadataV1Beta ¶
type CreateVersionMetadataV1Beta struct {
	// CloudBuildId: The Cloud Build ID if one was created as part of the version
	// create. @OutputOnly
	CloudBuildId string `json:"cloudBuildId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CloudBuildId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CloudBuildId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateVersionMetadataV1Beta: Metadata for the given google.longrunning.Operation during a google.appengine.v1beta.CreateVersionRequest.

func (CreateVersionMetadataV1Beta) MarshalJSON ¶
func (s CreateVersionMetadataV1Beta) MarshalJSON() ([]byte, error)
type CustomMetric ¶
type CustomMetric struct {
	// Filter: Allows filtering on the metric's fields.
	Filter string `json:"filter,omitempty"`
	// MetricName: The name of the metric.
	MetricName string `json:"metricName,omitempty"`
	// SingleInstanceAssignment: May be used instead of target_utilization when an
	// instance can handle a specific amount of work/resources and the metric value
	// is equal to the current amount of work remaining. The autoscaler will try to
	// keep the number of instances equal to the metric value divided by
	// single_instance_assignment.
	SingleInstanceAssignment float64 `json:"singleInstanceAssignment,omitempty"`
	// TargetType: The type of the metric. Must be a string representing a
	// Stackdriver metric type e.g. GAGUE, DELTA_PER_SECOND, etc.
	TargetType string `json:"targetType,omitempty"`
	// TargetUtilization: The target value for the metric.
	TargetUtilization float64 `json:"targetUtilization,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Filter") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Filter") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomMetric: Allows autoscaling based on Stackdriver metrics.

func (CustomMetric) MarshalJSON ¶
func (s CustomMetric) MarshalJSON() ([]byte, error)
func (*CustomMetric) UnmarshalJSON ¶
func (s *CustomMetric) UnmarshalJSON(data []byte) error
type Date ¶
added in v0.142.0
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

Date: Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: A full date, with non-zero year, month, and day values. A month and day, with a zero year (for example, an anniversary). A year on its own, with a zero month and a zero day. A year and month, with a zero day (for example, a credit card expiration date).Related types: google.type.TimeOfDay google.type.DateTime google.protobuf.Timestamp

func (Date) MarshalJSON ¶
added in v0.142.0
func (s Date) MarshalJSON() ([]byte, error)
type DebugInstanceRequest ¶
type DebugInstanceRequest struct {
	// SshKey: Public SSH key to add to the instance. Examples: [USERNAME]:ssh-rsa
	// [KEY_VALUE] [USERNAME] [USERNAME]:ssh-rsa [KEY_VALUE] google-ssh
	// {"userName":"[USERNAME]","expireOn":"[EXPIRE_TIME]"}For more information,
	// see Adding and Removing SSH Keys
	// (https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys).
	SshKey string `json:"sshKey,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SshKey") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SshKey") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DebugInstanceRequest: Request message for Instances.DebugInstance.

func (DebugInstanceRequest) MarshalJSON ¶
func (s DebugInstanceRequest) MarshalJSON() ([]byte, error)
type Deployment ¶
type Deployment struct {
	// Build: Google Cloud Build build information. Only applicable for instances
	// running in the App Engine flexible environment.
	Build *BuildInfo `json:"build,omitempty"`
	// CloudBuildOptions: Options for any Google Cloud Build builds created as a
	// part of this deployment.These options will only be used if a new build is
	// created, such as when deploying to the App Engine flexible environment using
	// files or zip.
	CloudBuildOptions *CloudBuildOptions `json:"cloudBuildOptions,omitempty"`
	// Container: The Docker image for the container that runs the version. Only
	// applicable for instances running in the App Engine flexible environment.
	Container *ContainerInfo `json:"container,omitempty"`
	// Files: Manifest of the files stored in Google Cloud Storage that are
	// included as part of this version. All files must be readable using the
	// credentials supplied with this call.
	Files map[string]FileInfo `json:"files,omitempty"`
	// Zip: The zip file for this deployment, if this is a zip deployment.
	Zip *ZipInfo `json:"zip,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Build") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Build") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Deployment: Code and application artifacts used to deploy a version to App Engine.

func (Deployment) MarshalJSON ¶
func (s Deployment) MarshalJSON() ([]byte, error)
type DiskUtilization ¶
type DiskUtilization struct {
	// TargetReadBytesPerSecond: Target bytes read per second.
	TargetReadBytesPerSecond int64 `json:"targetReadBytesPerSecond,omitempty"`
	// TargetReadOpsPerSecond: Target ops read per seconds.
	TargetReadOpsPerSecond int64 `json:"targetReadOpsPerSecond,omitempty"`
	// TargetWriteBytesPerSecond: Target bytes written per second.
	TargetWriteBytesPerSecond int64 `json:"targetWriteBytesPerSecond,omitempty"`
	// TargetWriteOpsPerSecond: Target ops written per second.
	TargetWriteOpsPerSecond int64 `json:"targetWriteOpsPerSecond,omitempty"`
	// ForceSendFields is a list of field names (e.g. "TargetReadBytesPerSecond")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "TargetReadBytesPerSecond") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DiskUtilization: Target scaling by disk usage. Only applicable in the App Engine flexible environment.

func (DiskUtilization) MarshalJSON ¶
func (s DiskUtilization) MarshalJSON() ([]byte, error)
type DomainMapping ¶
type DomainMapping struct {
	// Id: Relative name of the domain serving the application. Example:
	// example.com.
	Id string `json:"id,omitempty"`
	// Name: Output only. Full path to the DomainMapping resource in the API.
	// Example: apps/myapp/domainMapping/example.com.@OutputOnly
	Name string `json:"name,omitempty"`
	// ResourceRecords: Output only. The resource records required to configure
	// this domain mapping. These records must be added to the domain's DNS
	// configuration in order to serve the application via this domain
	// mapping.@OutputOnly
	ResourceRecords []*ResourceRecord `json:"resourceRecords,omitempty"`
	// SslSettings: SSL configuration for this domain. If unconfigured, this domain
	// will not serve with SSL.
	SslSettings *SslSettings `json:"sslSettings,omitempty"`

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

DomainMapping: A domain serving an App Engine application.

func (DomainMapping) MarshalJSON ¶
func (s DomainMapping) MarshalJSON() ([]byte, error)
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type EndpointsApiService ¶
type EndpointsApiService struct {
	// ConfigId: Endpoints service configuration ID as specified by the Service
	// Management API. For example "2016-09-19r1".By default, the rollout strategy
	// for Endpoints is RolloutStrategy.FIXED. This means that Endpoints starts up
	// with a particular configuration ID. When a new configuration is rolled out,
	// Endpoints must be given the new configuration ID. The config_id field is
	// used to give the configuration ID and is required in this case.Endpoints
	// also has a rollout strategy called RolloutStrategy.MANAGED. When using this,
	// Endpoints fetches the latest configuration and does not need the
	// configuration ID. In this case, config_id must be omitted.
	ConfigId string `json:"configId,omitempty"`
	// DisableTraceSampling: Enable or disable trace sampling. By default, this is
	// set to false for enabled.
	DisableTraceSampling bool `json:"disableTraceSampling,omitempty"`
	// Name: Endpoints service name which is the name of the "service" resource in
	// the Service Management API. For example
	// "myapi.endpoints.myproject.cloud.goog"
	Name string `json:"name,omitempty"`
	// RolloutStrategy: Endpoints rollout strategy. If FIXED, config_id must be
	// specified. If MANAGED, config_id must be omitted.
	//
	// Possible values:
	//   "UNSPECIFIED_ROLLOUT_STRATEGY" - Not specified. Defaults to FIXED.
	//   "FIXED" - Endpoints service configuration ID will be fixed to the
	// configuration ID specified by config_id.
	//   "MANAGED" - Endpoints service configuration ID will be updated with each
	// rollout.
	RolloutStrategy string `json:"rolloutStrategy,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ConfigId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConfigId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EndpointsApiService: Google Cloud Endpoints (https://cloud.google.com/endpoints) configuration. The Endpoints API Service provides tooling for serving Open API and gRPC endpoints via an NGINX proxy. Only valid for App Engine Flexible environment deployments.The fields here refer to the name and configuration ID of a "service" resource in the Service Management API (https://cloud.google.com/service-management/overview).

func (EndpointsApiService) MarshalJSON ¶
func (s EndpointsApiService) MarshalJSON() ([]byte, error)
type Entrypoint ¶
type Entrypoint struct {
	// Shell: The format should be a shell command that can be fed to bash -c.
	Shell string `json:"shell,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Shell") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Shell") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Entrypoint: The entrypoint for the application.

func (Entrypoint) MarshalJSON ¶
func (s Entrypoint) MarshalJSON() ([]byte, error)
type ErrorHandler ¶
type ErrorHandler struct {
	// ErrorCode: Error condition this handler applies to.
	//
	// Possible values:
	//   "ERROR_CODE_UNSPECIFIED" - Not specified. ERROR_CODE_DEFAULT is assumed.
	//   "ERROR_CODE_DEFAULT" - All other error types.
	//   "ERROR_CODE_OVER_QUOTA" - Application has exceeded a resource quota.
	//   "ERROR_CODE_DOS_API_DENIAL" - Client blocked by the application's Denial
	// of Service protection configuration.
	//   "ERROR_CODE_TIMEOUT" - Deadline reached before the application responds.
	ErrorCode string `json:"errorCode,omitempty"`
	// MimeType: MIME type of file. Defaults to text/html.
	MimeType string `json:"mimeType,omitempty"`
	// StaticFile: Static file content to be served for this error.
	StaticFile string `json:"staticFile,omitempty"`
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

ErrorHandler: Custom static error page to be served when an error occurs.

func (ErrorHandler) MarshalJSON ¶
func (s ErrorHandler) MarshalJSON() ([]byte, error)
type FeatureSettings ¶
type FeatureSettings struct {
	// SplitHealthChecks: Boolean value indicating if split health checks should be
	// used instead of the legacy health checks. At an app.yaml level, this means
	// defaulting to 'readiness_check' and 'liveness_check' values instead of
	// 'health_check' ones. Once the legacy 'health_check' behavior is deprecated,
	// and this value is always true, this setting can be removed.
	SplitHealthChecks bool `json:"splitHealthChecks,omitempty"`
	// UseContainerOptimizedOs: If true, use Container-Optimized OS
	// (https://cloud.google.com/container-optimized-os/) base image for VMs,
	// rather than a base Debian image.
	UseContainerOptimizedOs bool `json:"useContainerOptimizedOs,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SplitHealthChecks") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SplitHealthChecks") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FeatureSettings: The feature specific settings to be used in the application. These define behaviors that are user configurable.

func (FeatureSettings) MarshalJSON ¶
func (s FeatureSettings) MarshalJSON() ([]byte, error)
type FileInfo ¶
type FileInfo struct {
	// MimeType: The MIME type of the file.Defaults to the value from Google Cloud
	// Storage.
	MimeType string `json:"mimeType,omitempty"`
	// Sha1Sum: The SHA1 hash of the file, in hex.
	Sha1Sum string `json:"sha1Sum,omitempty"`
	// SourceUrl: URL source to use to fetch this file. Must be a URL to a resource
	// in Google Cloud Storage in the form 'http(s)://storage.googleapis.com//'.
	SourceUrl string `json:"sourceUrl,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MimeType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MimeType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FileInfo: Single source file that is part of the version to be deployed. Each source file that is deployed must be specified separately.

func (FileInfo) MarshalJSON ¶
func (s FileInfo) MarshalJSON() ([]byte, error)
type FirewallRule ¶
type FirewallRule struct {
	// Action: The action to take on matched requests.
	//
	// Possible values:
	//   "UNSPECIFIED_ACTION"
	//   "ALLOW" - Matching requests are allowed.
	//   "DENY" - Matching requests are denied.
	Action string `json:"action,omitempty"`
	// Description: An optional string description of this rule. This field has a
	// maximum length of 400 characters.
	Description string `json:"description,omitempty"`
	Priority    int64  `json:"priority,omitempty"`
	// SourceRange: IP address or range, defined using CIDR notation, of requests
	// that this rule applies to. You can use the wildcard character "*" to match
	// all IPs equivalent to "0/0" and "::/0" together. Examples: 192.168.1.1 or
	// 192.168.0.0/16 or 2001:db8::/32 or 2001:0db8:0000:0042:0000:8a2e:0370:7334.
	// Truncation will be silently performed on addresses which are not properly
	// truncated. For example, 1.2.3.4/24 is accepted as the same address as
	// 1.2.3.0/24. Similarly, for IPv6, 2001:db8::1/32 is accepted as the same
	// address as 2001:db8::/32.
	SourceRange string `json:"sourceRange,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

FirewallRule: A single firewall rule that is evaluated against incoming traffic and provides an action to take on matched requests. A positive integer between 1, Int32.MaxValue-1 that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user.

func (FirewallRule) MarshalJSON ¶
func (s FirewallRule) MarshalJSON() ([]byte, error)
type FlexibleRuntimeSettings ¶
added in v0.109.0
type FlexibleRuntimeSettings struct {
	// OperatingSystem: The operating system of the application runtime.
	OperatingSystem string `json:"operatingSystem,omitempty"`
	// RuntimeVersion: The runtime version of an App Engine flexible application.
	RuntimeVersion string `json:"runtimeVersion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OperatingSystem") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OperatingSystem") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FlexibleRuntimeSettings: Runtime settings for the App Engine flexible environment.

func (FlexibleRuntimeSettings) MarshalJSON ¶
added in v0.109.0
func (s FlexibleRuntimeSettings) MarshalJSON() ([]byte, error)
type GceTag ¶
added in v0.197.0
type GceTag struct {
	// Parent: The parents(s) of the tag. Eg. projects/123, folders/456 It usually
	// contains only one parent. But, in some corner cases, it can contain multiple
	// parents. Currently, organizations are not supported.
	Parent []string `json:"parent,omitempty"`
	// Tag: The administrative_tag name.
	Tag string `json:"tag,omitempty"`
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

GceTag: For use only by GCE. GceTag is a wrapper around the GCE administrative tag with parent info.

func (GceTag) MarshalJSON ¶
added in v0.197.0
func (s GceTag) MarshalJSON() ([]byte, error)
type GoogleAppengineV1betaLocationMetadata ¶
added in v0.46.0
type GoogleAppengineV1betaLocationMetadata struct {
	// FlexibleEnvironmentAvailable: App Engine flexible environment is available
	// in the given location.@OutputOnly
	FlexibleEnvironmentAvailable bool `json:"flexibleEnvironmentAvailable,omitempty"`
	// SearchApiAvailable: Output only. Search API
	// (https://cloud.google.com/appengine/docs/standard/python/search) is
	// available in the given location.
	SearchApiAvailable bool `json:"searchApiAvailable,omitempty"`
	// StandardEnvironmentAvailable: App Engine standard environment is available
	// in the given location.@OutputOnly
	StandardEnvironmentAvailable bool `json:"standardEnvironmentAvailable,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "FlexibleEnvironmentAvailable") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FlexibleEnvironmentAvailable") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAppengineV1betaLocationMetadata: Metadata for the given google.cloud.location.Location.

func (GoogleAppengineV1betaLocationMetadata) MarshalJSON ¶
added in v0.46.0
func (s GoogleAppengineV1betaLocationMetadata) MarshalJSON() ([]byte, error)
type HealthCheck ¶
type HealthCheck struct {
	// CheckInterval: Interval between health checks.
	CheckInterval string `json:"checkInterval,omitempty"`
	// DisableHealthCheck: Whether to explicitly disable health checks for this
	// instance.
	DisableHealthCheck bool `json:"disableHealthCheck,omitempty"`
	// HealthyThreshold: Number of consecutive successful health checks required
	// before receiving traffic.
	HealthyThreshold int64 `json:"healthyThreshold,omitempty"`
	// Host: Host header to send when performing an HTTP health check. Example:
	// "myapp.appspot.com"
	Host string `json:"host,omitempty"`
	// RestartThreshold: Number of consecutive failed health checks required before
	// an instance is restarted.
	RestartThreshold int64 `json:"restartThreshold,omitempty"`
	// Timeout: Time before the health check is considered failed.
	Timeout string `json:"timeout,omitempty"`
	// UnhealthyThreshold: Number of consecutive failed health checks required
	// before removing traffic.
	UnhealthyThreshold int64 `json:"unhealthyThreshold,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CheckInterval") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CheckInterval") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

HealthCheck: Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances. Only applicable for instances in App Engine flexible environment.

func (HealthCheck) MarshalJSON ¶
func (s HealthCheck) MarshalJSON() ([]byte, error)
type IdentityAwareProxy ¶
type IdentityAwareProxy struct {
	// Enabled: Whether the serving infrastructure will authenticate and authorize
	// all incoming requests.If true, the oauth2_client_id and oauth2_client_secret
	// fields must be non-empty.
	Enabled bool `json:"enabled,omitempty"`
	// Oauth2ClientId: OAuth2 client ID to use for the authentication flow.
	Oauth2ClientId string `json:"oauth2ClientId,omitempty"`
	// Oauth2ClientSecret: OAuth2 client secret to use for the authentication
	// flow.For security reasons, this value cannot be retrieved via the API.
	// Instead, the SHA-256 hash of the value is returned in the
	// oauth2_client_secret_sha256 field.@InputOnly
	Oauth2ClientSecret string `json:"oauth2ClientSecret,omitempty"`
	// Oauth2ClientSecretSha256: Output only. Hex-encoded SHA-256 hash of the
	// client secret.@OutputOnly
	Oauth2ClientSecretSha256 string `json:"oauth2ClientSecretSha256,omitempty"`
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

IdentityAwareProxy: Identity-Aware Proxy

func (IdentityAwareProxy) MarshalJSON ¶
func (s IdentityAwareProxy) MarshalJSON() ([]byte, error)
type Instance ¶
type Instance struct {
	// AppEngineRelease: Output only. App Engine release this instance is running
	// on.
	AppEngineRelease string `json:"appEngineRelease,omitempty"`
	// Availability: Output only. Availability of the instance.
	//
	// Possible values:
	//   "UNSPECIFIED"
	//   "RESIDENT"
	//   "DYNAMIC"
	Availability string `json:"availability,omitempty"`
	// AverageLatency: Output only. Average latency (ms) over the last minute.
	AverageLatency int64 `json:"averageLatency,omitempty"`
	// Errors: Output only. Number of errors since this instance was started.
	Errors int64 `json:"errors,omitempty"`
	// Id: Output only. Relative name of the instance within the version. Example:
	// instance-1.
	Id string `json:"id,omitempty"`
	// MemoryUsage: Output only. Total memory in use (bytes).
	MemoryUsage int64 `json:"memoryUsage,omitempty,string"`
	// Name: Output only. Full path to the Instance resource in the API. Example:
	// apps/myapp/services/default/versions/v1/instances/instance-1.
	Name string `json:"name,omitempty"`
	// Qps: Output only. Average queries per second (QPS) over the last minute.
	Qps float64 `json:"qps,omitempty"`
	// Requests: Output only. Number of requests since this instance was started.
	Requests int64 `json:"requests,omitempty"`
	// StartTime: Output only. Time that this instance was started.@OutputOnly
	StartTime string `json:"startTime,omitempty"`
	// VmDebugEnabled: Output only. Whether this instance is in debug mode. Only
	// applicable for instances in App Engine flexible environment.
	VmDebugEnabled bool `json:"vmDebugEnabled,omitempty"`
	// VmId: Output only. Virtual machine ID of this instance. Only applicable for
	// instances in App Engine flexible environment.
	VmId string `json:"vmId,omitempty"`
	// VmIp: Output only. The IP address of this instance. Only applicable for
	// instances in App Engine flexible environment.
	VmIp string `json:"vmIp,omitempty"`
	// VmLiveness: Output only. The liveness health check of this instance. Only
	// applicable for instances in App Engine flexible environment.
	//
	// Possible values:
	//   "LIVENESS_STATE_UNSPECIFIED" - There is no liveness health check for the
	// instance. Only applicable for instances in App Engine standard environment.
	//   "UNKNOWN" - The health checking system is aware of the instance but its
	// health is not known at the moment.
	//   "HEALTHY" - The instance is reachable i.e. a connection to the application
	// health checking endpoint can be established, and conforms to the
	// requirements defined by the health check.
	//   "UNHEALTHY" - The instance is reachable, but does not conform to the
	// requirements defined by the health check.
	//   "DRAINING" - The instance is being drained. The existing connections to
	// the instance have time to complete, but the new ones are being refused.
	//   "TIMEOUT" - The instance is unreachable i.e. a connection to the
	// application health checking endpoint cannot be established, or the server
	// does not respond within the specified timeout.
	VmLiveness string `json:"vmLiveness,omitempty"`
	// VmName: Output only. Name of the virtual machine where this instance lives.
	// Only applicable for instances in App Engine flexible environment.
	VmName string `json:"vmName,omitempty"`
	// VmStatus: Output only. Status of the virtual machine where this instance
	// lives. Only applicable for instances in App Engine flexible environment.
	VmStatus string `json:"vmStatus,omitempty"`
	// VmZoneName: Output only. Zone where the virtual machine is located. Only
	// applicable for instances in App Engine flexible environment.
	VmZoneName string `json:"vmZoneName,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppEngineRelease") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppEngineRelease") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Instance: An Instance resource is the computing unit that App Engine uses to automatically scale an application.

func (Instance) MarshalJSON ¶
func (s Instance) MarshalJSON() ([]byte, error)
func (*Instance) UnmarshalJSON ¶
func (s *Instance) UnmarshalJSON(data []byte) error
type Library ¶
type Library struct {
	// Name: Name of the library. Example: "django".
	Name string `json:"name,omitempty"`
	// Version: Version of the library to select, or "latest".
	Version string `json:"version,omitempty"`
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

Library: Third-party Python runtime library that is required by the application.

func (Library) MarshalJSON ¶
func (s Library) MarshalJSON() ([]byte, error)
type ListAuthorizedCertificatesResponse ¶
type ListAuthorizedCertificatesResponse struct {
	// Certificates: The SSL certificates the user is authorized to administer.
	Certificates []*AuthorizedCertificate `json:"certificates,omitempty"`
	// NextPageToken: Continuation token for fetching the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Certificates") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Certificates") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListAuthorizedCertificatesResponse: Response message for AuthorizedCertificates.ListAuthorizedCertificates.

func (ListAuthorizedCertificatesResponse) MarshalJSON ¶
func (s ListAuthorizedCertificatesResponse) MarshalJSON() ([]byte, error)
type ListAuthorizedDomainsResponse ¶
type ListAuthorizedDomainsResponse struct {
	// Domains: The authorized domains belonging to the user.
	Domains []*AuthorizedDomain `json:"domains,omitempty"`
	// NextPageToken: Continuation token for fetching the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

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

ListAuthorizedDomainsResponse: Response message for AuthorizedDomains.ListAuthorizedDomains.

func (ListAuthorizedDomainsResponse) MarshalJSON ¶
func (s ListAuthorizedDomainsResponse) MarshalJSON() ([]byte, error)
type ListDomainMappingsResponse ¶
type ListDomainMappingsResponse struct {
	// DomainMappings: The domain mappings for the application.
	DomainMappings []*DomainMapping `json:"domainMappings,omitempty"`
	// NextPageToken: Continuation token for fetching the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DomainMappings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DomainMappings") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListDomainMappingsResponse: Response message for DomainMappings.ListDomainMappings.

func (ListDomainMappingsResponse) MarshalJSON ¶
func (s ListDomainMappingsResponse) MarshalJSON() ([]byte, error)
type ListIngressRulesResponse ¶
type ListIngressRulesResponse struct {
	// IngressRules: The ingress FirewallRules for this application.
	IngressRules []*FirewallRule `json:"ingressRules,omitempty"`
	// NextPageToken: Continuation token for fetching the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "IngressRules") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IngressRules") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListIngressRulesResponse: Response message for Firewall.ListIngressRules.

func (ListIngressRulesResponse) MarshalJSON ¶
func (s ListIngressRulesResponse) MarshalJSON() ([]byte, error)
type ListInstancesResponse ¶
type ListInstancesResponse struct {
	// Instances: The instances belonging to the requested version.
	Instances []*Instance `json:"instances,omitempty"`
	// NextPageToken: Continuation token for fetching the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

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

ListInstancesResponse: Response message for Instances.ListInstances.

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
type ListOperationsResponse ¶
type ListOperationsResponse struct {
	// NextPageToken: The standard List next-page token.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Operations: A list of operations that matches the specified filter in the
	// request.
	Operations []*Operation `json:"operations,omitempty"`
	// Unreachable: Unordered list. Unreachable resources. Populated when the
	// request sets ListOperationsRequest.return_partial_success and reads across
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
type ListRuntimesResponse ¶
added in v0.137.0
type ListRuntimesResponse struct {
	// NextPageToken: Continuation token for fetching the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Runtimes: The runtimes available to the requested application.
	Runtimes []*Runtime `json:"runtimes,omitempty"`

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

ListRuntimesResponse: Response message for Applications.ListRuntimes.

func (ListRuntimesResponse) MarshalJSON ¶
added in v0.137.0
func (s ListRuntimesResponse) MarshalJSON() ([]byte, error)
type ListServicesResponse ¶
type ListServicesResponse struct {
	// NextPageToken: Continuation token for fetching the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Services: The services belonging to the requested application.
	Services []*Service `json:"services,omitempty"`

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

ListServicesResponse: Response message for Services.ListServices.

func (ListServicesResponse) MarshalJSON ¶
func (s ListServicesResponse) MarshalJSON() ([]byte, error)
type ListVersionsResponse ¶
type ListVersionsResponse struct {
	// NextPageToken: Continuation token for fetching the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Versions: The versions belonging to the requested service.
	Versions []*Version `json:"versions,omitempty"`

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

ListVersionsResponse: Response message for Versions.ListVersions.

func (ListVersionsResponse) MarshalJSON ¶
func (s ListVersionsResponse) MarshalJSON() ([]byte, error)
type LivenessCheck ¶
type LivenessCheck struct {
	// CheckInterval: Interval between health checks.
	CheckInterval string `json:"checkInterval,omitempty"`
	// FailureThreshold: Number of consecutive failed checks required before
	// considering the VM unhealthy.
	FailureThreshold int64 `json:"failureThreshold,omitempty"`
	// Host: Host header to send when performing a HTTP Liveness check. Example:
	// "myapp.appspot.com"
	Host string `json:"host,omitempty"`
	// InitialDelay: The initial delay before starting to execute the checks.
	InitialDelay string `json:"initialDelay,omitempty"`
	// Path: The request path.
	Path string `json:"path,omitempty"`
	// SuccessThreshold: Number of consecutive successful checks required before
	// considering the VM healthy.
	SuccessThreshold int64 `json:"successThreshold,omitempty"`
	// Timeout: Time before the check is considered failed.
	Timeout string `json:"timeout,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CheckInterval") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CheckInterval") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LivenessCheck: Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.

func (LivenessCheck) MarshalJSON ¶
func (s LivenessCheck) MarshalJSON() ([]byte, error)
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
	// implementations. For example: "projects/example-project/locations/us-east1"
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
type LocationMetadata struct {
	// FlexibleEnvironmentAvailable: App Engine flexible environment is available
	// in the given location.@OutputOnly
	FlexibleEnvironmentAvailable bool `json:"flexibleEnvironmentAvailable,omitempty"`
	// SearchApiAvailable: Output only. Search API
	// (https://cloud.google.com/appengine/docs/standard/python/search) is
	// available in the given location.
	SearchApiAvailable bool `json:"searchApiAvailable,omitempty"`
	// StandardEnvironmentAvailable: App Engine standard environment is available
	// in the given location.@OutputOnly
	StandardEnvironmentAvailable bool `json:"standardEnvironmentAvailable,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "FlexibleEnvironmentAvailable") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FlexibleEnvironmentAvailable") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LocationMetadata: Metadata for the given google.cloud.location.Location.

func (LocationMetadata) MarshalJSON ¶
func (s LocationMetadata) MarshalJSON() ([]byte, error)
type ManagedCertificate ¶
type ManagedCertificate struct {
	// LastRenewalTime: Time at which the certificate was last renewed. The renewal
	// process is fully managed. Certificate renewal will automatically occur
	// before the certificate expires. Renewal errors can be tracked via
	// ManagementStatus.@OutputOnly
	LastRenewalTime string `json:"lastRenewalTime,omitempty"`
	// Status: Status of certificate management. Refers to the most recent
	// certificate acquisition or renewal attempt.@OutputOnly
	//
	// Possible values:
	//   "MANAGEMENT_STATUS_UNSPECIFIED"
	//   "OK" - Certificate was successfully obtained and inserted into the serving
	// system.
	//   "PENDING" - Certificate is under active attempts to acquire or renew.
	//   "FAILED_RETRYING_NOT_VISIBLE" - Most recent renewal failed due to an
	// invalid DNS setup and will be retried. Renewal attempts will continue to
	// fail until the certificate domain's DNS configuration is fixed. The last
	// successfully provisioned certificate may still be serving.
	//   "FAILED_PERMANENT" - All renewal attempts have been exhausted, likely due
	// to an invalid DNS setup.
	//   "FAILED_RETRYING_CAA_FORBIDDEN" - Most recent renewal failed due to an
	// explicit CAA record that does not include one of the in-use CAs (Google CA
	// and Let's Encrypt). Renewals will continue to fail until the CAA is
	// reconfigured. The last successfully provisioned certificate may still be
	// serving.
	//   "FAILED_RETRYING_CAA_CHECKING" - Most recent renewal failed due to a CAA
	// retrieval failure. This means that the domain's DNS provider does not
	// properly handle CAA records, failing requests for CAA records when no CAA
	// records are defined. Renewals will continue to fail until the DNS provider
	// is changed or a CAA record is added for the given domain. The last
	// successfully provisioned certificate may still be serving.
	Status string `json:"status,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LastRenewalTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LastRenewalTime") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ManagedCertificate: A certificate managed by App Engine.

func (ManagedCertificate) MarshalJSON ¶
func (s ManagedCertificate) MarshalJSON() ([]byte, error)
type ManualScaling ¶
type ManualScaling struct {
	// Instances: Number of instances to assign to the service at the start. This
	// number can later be altered by using the Modules API
	// (https://cloud.google.com/appengine/docs/python/modules/functions)
	// set_num_instances() function.
	Instances int64 `json:"instances,omitempty"`
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

ManualScaling: A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.

func (ManualScaling) MarshalJSON ¶
func (s ManualScaling) MarshalJSON() ([]byte, error)
type Network ¶
type Network struct {
	// ForwardedPorts: List of ports, or port pairs, to forward from the virtual
	// machine to the application container. Only applicable in the App Engine
	// flexible environment.
	ForwardedPorts []string `json:"forwardedPorts,omitempty"`
	// InstanceIpMode: The IP mode for instances. Only applicable in the App Engine
	// flexible environment.
	//
	// Possible values:
	//   "INSTANCE_IP_MODE_UNSPECIFIED" - Unspecified is treated as EXTERNAL.
	//   "EXTERNAL" - Instances are created with both internal and external IP
	// addresses.
	//   "INTERNAL" - Instances are created with internal IP addresses only.
	InstanceIpMode string `json:"instanceIpMode,omitempty"`
	// InstanceTag: Tag to apply to the instance during creation. Only applicable
	// in the App Engine flexible environment.
	InstanceTag string `json:"instanceTag,omitempty"`
	// Name: Google Compute Engine network where the virtual machines are created.
	// Specify the short name, not the resource path.Defaults to default.
	Name string `json:"name,omitempty"`
	// SessionAffinity: Enable session affinity. Only applicable in the App Engine
	// flexible environment.
	SessionAffinity bool `json:"sessionAffinity,omitempty"`
	// SubnetworkName: Google Cloud Platform sub-network where the virtual machines
	// are created. Specify the short name, not the resource path.If a subnetwork
	// name is specified, a network name will also be required unless it is for the
	// default network. If the network that the instance is being created in is a
	// Legacy network, then the IP address is allocated from the IPv4Range. If the
	// network that the instance is being created in is an auto Subnet Mode
	// Network, then only network name should be specified (not the
	// subnetwork_name) and the IP address is created from the IPCidrRange of the
	// subnetwork that exists in that zone for that network. If the network that
	// the instance is being created in is a custom Subnet Mode Network, then the
	// subnetwork_name must be specified and the IP address is created from the
	// IPCidrRange of the subnetwork.If specified, the subnetwork must exist in the
	// same region as the App Engine flexible environment application.
	SubnetworkName string `json:"subnetworkName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ForwardedPorts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ForwardedPorts") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Network: Extra network settings. Only applicable in the App Engine flexible environment.

func (Network) MarshalJSON ¶
func (s Network) MarshalJSON() ([]byte, error)
type NetworkSettings ¶
added in v0.32.0
type NetworkSettings struct {
	// IngressTrafficAllowed: The ingress settings for version or service.
	//
	// Possible values:
	//   "INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED" - Unspecified
	//   "INGRESS_TRAFFIC_ALLOWED_ALL" - Allow HTTP traffic from public and private
	// sources.
	//   "INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY" - Allow HTTP traffic from only
	// private VPC sources.
	//   "INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB" - Allow HTTP traffic from
	// private VPC sources and through load balancers.
	IngressTrafficAllowed string `json:"ingressTrafficAllowed,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IngressTrafficAllowed") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IngressTrafficAllowed") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NetworkSettings: A NetworkSettings resource is a container for ingress settings for a version or service.

func (NetworkSettings) MarshalJSON ¶
added in v0.32.0
func (s NetworkSettings) MarshalJSON() ([]byte, error)
type NetworkUtilization ¶
type NetworkUtilization struct {
	// TargetReceivedBytesPerSecond: Target bytes received per second.
	TargetReceivedBytesPerSecond int64 `json:"targetReceivedBytesPerSecond,omitempty"`
	// TargetReceivedPacketsPerSecond: Target packets received per second.
	TargetReceivedPacketsPerSecond int64 `json:"targetReceivedPacketsPerSecond,omitempty"`
	// TargetSentBytesPerSecond: Target bytes sent per second.
	TargetSentBytesPerSecond int64 `json:"targetSentBytesPerSecond,omitempty"`
	// TargetSentPacketsPerSecond: Target packets sent per second.
	TargetSentPacketsPerSecond int64 `json:"targetSentPacketsPerSecond,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "TargetReceivedBytesPerSecond") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "TargetReceivedBytesPerSecond") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NetworkUtilization: Target scaling by network usage. Only applicable in the App Engine flexible environment.

func (NetworkUtilization) MarshalJSON ¶
func (s NetworkUtilization) MarshalJSON() ([]byte, error)
type Operation ¶
type Operation struct {
	// Done: If the value is false, it means the operation is still in progress. If
	// true, the operation is completed, and either error or response is available.
	Done bool `json:"done,omitempty"`
	// Error: The error result of the operation in case of failure or cancellation.
	Error *Status `json:"error,omitempty"`
	// Metadata: Service-specific metadata associated with the operation. It
	// typically contains progress information and common metadata such as create
	// time. Some services might not provide such metadata. Any method that returns
	// a long-running operation should document the metadata type, if any.
	Metadata googleapi.RawMessage `json:"metadata,omitempty"`
	// Name: The server-assigned name, which is only unique within the same service
	// that originally returns it. If you use the default HTTP mapping, the name
	// should be a resource name ending with operations/{unique_id}.
	Name string `json:"name,omitempty"`
	// Response: The normal, successful response of the operation. If the original
	// method returns no data on success, such as Delete, the response is
	// google.protobuf.Empty. If the original method is standard Get/Create/Update,
	// the response should be the resource. For other methods, the response should
	// have the type XxxResponse, where Xxx is the original method name. For
	// example, if the original method name is TakeSnapshot(), the inferred
	// response type is TakeSnapshotResponse.
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
type OperationMetadataV1 ¶
type OperationMetadataV1 struct {
	CreateVersionMetadata *CreateVersionMetadataV1 `json:"createVersionMetadata,omitempty"`
	// EndTime: Time that this operation completed.@OutputOnly
	EndTime string `json:"endTime,omitempty"`
	// EphemeralMessage: Ephemeral message that may change every time the operation
	// is polled. @OutputOnly
	EphemeralMessage string `json:"ephemeralMessage,omitempty"`
	// InsertTime: Time that this operation was created.@OutputOnly
	InsertTime string `json:"insertTime,omitempty"`
	// Method: API method that initiated this operation. Example:
	// google.appengine.v1.Versions.CreateVersion.@OutputOnly
	Method string `json:"method,omitempty"`
	// Target: Name of the resource that this operation is acting on. Example:
	// apps/myapp/services/default.@OutputOnly
	Target string `json:"target,omitempty"`
	// User: User who requested this operation.@OutputOnly
	User string `json:"user,omitempty"`
	// Warning: Durable messages that persist on every operation poll. @OutputOnly
	Warning []string `json:"warning,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CreateVersionMetadata") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateVersionMetadata") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OperationMetadataV1: Metadata for the given google.longrunning.Operation.

func (OperationMetadataV1) MarshalJSON ¶
func (s OperationMetadataV1) MarshalJSON() ([]byte, error)
type OperationMetadataV1Alpha ¶
type OperationMetadataV1Alpha struct {
	CreateVersionMetadata *CreateVersionMetadataV1Alpha `json:"createVersionMetadata,omitempty"`
	// EndTime: Time that this operation completed.@OutputOnly
	EndTime string `json:"endTime,omitempty"`
	// EphemeralMessage: Ephemeral message that may change every time the operation
	// is polled. @OutputOnly
	EphemeralMessage string `json:"ephemeralMessage,omitempty"`
	// InsertTime: Time that this operation was created.@OutputOnly
	InsertTime string `json:"insertTime,omitempty"`
	// Method: API method that initiated this operation. Example:
	// google.appengine.v1alpha.Versions.CreateVersion.@OutputOnly
	Method string `json:"method,omitempty"`
	// Target: Name of the resource that this operation is acting on. Example:
	// apps/myapp/services/default.@OutputOnly
	Target string `json:"target,omitempty"`
	// User: User who requested this operation.@OutputOnly
	User string `json:"user,omitempty"`
	// Warning: Durable messages that persist on every operation poll. @OutputOnly
	Warning []string `json:"warning,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CreateVersionMetadata") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateVersionMetadata") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OperationMetadataV1Alpha: Metadata for the given google.longrunning.Operation.

func (OperationMetadataV1Alpha) MarshalJSON ¶
func (s OperationMetadataV1Alpha) MarshalJSON() ([]byte, error)
type OperationMetadataV1Beta ¶
type OperationMetadataV1Beta struct {
	CreateVersionMetadata *CreateVersionMetadataV1Beta `json:"createVersionMetadata,omitempty"`
	// EndTime: Time that this operation completed.@OutputOnly
	EndTime string `json:"endTime,omitempty"`
	// EphemeralMessage: Ephemeral message that may change every time the operation
	// is polled. @OutputOnly
	EphemeralMessage string `json:"ephemeralMessage,omitempty"`
	// InsertTime: Time that this operation was created.@OutputOnly
	InsertTime string `json:"insertTime,omitempty"`
	// Method: API method that initiated this operation. Example:
	// google.appengine.v1beta.Versions.CreateVersion.@OutputOnly
	Method string `json:"method,omitempty"`
	// Target: Name of the resource that this operation is acting on. Example:
	// apps/myapp/services/default.@OutputOnly
	Target string `json:"target,omitempty"`
	// User: User who requested this operation.@OutputOnly
	User string `json:"user,omitempty"`
	// Warning: Durable messages that persist on every operation poll. @OutputOnly
	Warning []string `json:"warning,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CreateVersionMetadata") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateVersionMetadata") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OperationMetadataV1Beta: Metadata for the given google.longrunning.Operation.

func (OperationMetadataV1Beta) MarshalJSON ¶
func (s OperationMetadataV1Beta) MarshalJSON() ([]byte, error)
type ProjectEvent ¶
added in v0.105.0
type ProjectEvent struct {
	// EventId: The unique ID for this project event. CLHs can use this value to
	// dedup repeated calls. required
	EventId string `json:"eventId,omitempty"`
	// Phase: Phase indicates when in the container event propagation this event is
	// being communicated. Events are sent before and after the per-resource events
	// are propagated. required
	//
	// Possible values:
	//   "CONTAINER_EVENT_PHASE_UNSPECIFIED"
	//   "BEFORE_RESOURCE_HANDLING"
	//   "AFTER_RESOURCE_HANDLING"
	Phase string `json:"phase,omitempty"`
	// ProjectMetadata: The projects metadata for this project. required
	ProjectMetadata *ProjectsMetadata `json:"projectMetadata,omitempty"`
	// State: The state of the organization that led to this event.
	State *ContainerState `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EventId") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProjectEvent: The request sent to CLHs during project events.

func (ProjectEvent) MarshalJSON ¶
added in v0.105.0
func (s ProjectEvent) MarshalJSON() ([]byte, error)
type ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall ¶
added in v0.238.0
type ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Context ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Do ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)

Do executes the "appengine.projects.locations.applications.authorizedCertificates.create" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Fields ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Header ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall ¶
added in v0.238.0
type ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Context ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Do ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "appengine.projects.locations.applications.authorizedCertificates.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Fields ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Header ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsAuthorizedCertificatesGetCall ¶
added in v0.238.0
type ProjectsLocationsApplicationsAuthorizedCertificatesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Context ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Do ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)

Do executes the "appengine.projects.locations.applications.authorizedCertificates.get" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Fields ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Header ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) IfNoneMatch ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) View ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) View(view string) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall

View sets the optional parameter "view": Controls the set of fields returned in the GET response.

Possible values:

"BASIC_CERTIFICATE" - Basic certificate information, including applicable


domains and expiration date.

"FULL_CERTIFICATE" - The information from BASIC_CERTIFICATE, plus detailed


information on the domain mappings that have this certificate mapped.

type ProjectsLocationsApplicationsAuthorizedCertificatesListCall ¶
added in v0.238.0
type ProjectsLocationsApplicationsAuthorizedCertificatesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Context ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Do ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedCertificatesResponse, error)

Do executes the "appengine.projects.locations.applications.authorizedCertificates.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuthorizedCertificatesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Fields ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Header ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesListCall) IfNoneMatch ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesListCall) PageSize ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesListCall) PageToken ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Pages ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Pages(ctx context.Context, f func(*ListAuthorizedCertificatesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesListCall) View ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) View(view string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall

View sets the optional parameter "view": Controls the set of fields returned in the LIST response.

Possible values:

"BASIC_CERTIFICATE" - Basic certificate information, including applicable


domains and expiration date.

"FULL_CERTIFICATE" - The information from BASIC_CERTIFICATE, plus detailed


information on the domain mappings that have this certificate mapped.

type ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall ¶
added in v0.238.0
type ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Context ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Do ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)

Do executes the "appengine.projects.locations.applications.authorizedCertificates.patch" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Fields ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Header ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) UpdateMask ¶
added in v0.238.0
func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall

UpdateMask sets the optional parameter "updateMask": Standard field mask for the set of fields to be updated. Updates are only supported on the certificate_raw_data and display_name fields.

type ProjectsLocationsApplicationsAuthorizedCertificatesService ¶
added in v0.238.0
type ProjectsLocationsApplicationsAuthorizedCertificatesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsAuthorizedCertificatesService ¶
added in v0.238.0
func NewProjectsLocationsApplicationsAuthorizedCertificatesService(s *APIService) *ProjectsLocationsApplicationsAuthorizedCertificatesService
func (*ProjectsLocationsApplicationsAuthorizedCertificatesService) Create ¶
added in v0.238.0
func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Create(projectsId string, locationsId string, applicationsId string, authorizedcertificate *AuthorizedCertificate) *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall

Create: Uploads the specified SSL certificate.

applicationsId: Part of `parent`. See documentation of `projectsId`.
locationsId: Part of `parent`. See documentation of `projectsId`.
projectsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
func (*ProjectsLocationsApplicationsAuthorizedCertificatesService) Delete ¶
added in v0.238.0
func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Delete(projectsId string, locationsId string, applicationsId string, authorizedCertificatesId string) *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall

Delete: Deletes the specified SSL certificate.

applicationsId: Part of `name`. See documentation of `projectsId`.
authorizedCertificatesId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource to delete. Example: apps/myapp/authorizedCertificates/12345.
func (*ProjectsLocationsApplicationsAuthorizedCertificatesService) Get ¶
added in v0.238.0
func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Get(projectsId string, locationsId string, applicationsId string, authorizedCertificatesId string) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall

Get: Gets the specified SSL certificate.

applicationsId: Part of `name`. See documentation of `projectsId`.
authorizedCertificatesId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource requested. Example: apps/myapp/authorizedCertificates/12345.
func (*ProjectsLocationsApplicationsAuthorizedCertificatesService) List ¶
added in v0.238.0
func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) List(projectsId string, locationsId string, applicationsId string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall

List: Lists all SSL certificates the user is authorized to administer.

applicationsId: Part of `parent`. See documentation of `projectsId`.
locationsId: Part of `parent`. See documentation of `projectsId`.
projectsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
func (*ProjectsLocationsApplicationsAuthorizedCertificatesService) Patch ¶
added in v0.238.0
func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Patch(projectsId string, locationsId string, applicationsId string, authorizedCertificatesId string, authorizedcertificate *AuthorizedCertificate) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall

Patch: Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update certificate_data with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate display_name may also be updated.

applicationsId: Part of `name`. See documentation of `projectsId`.
authorizedCertificatesId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource to update. Example: apps/myapp/authorizedCertificates/12345.
type ProjectsLocationsApplicationsAuthorizedDomainsListCall ¶
added in v0.168.0
type ProjectsLocationsApplicationsAuthorizedDomainsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) Context ¶
added in v0.168.0
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedDomainsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) Do ¶
added in v0.168.0
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedDomainsResponse, error)

Do executes the "appengine.projects.locations.applications.authorizedDomains.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuthorizedDomainsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) Fields ¶
added in v0.168.0
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedDomainsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) Header ¶
added in v0.168.0
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) IfNoneMatch ¶
added in v0.168.0
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsAuthorizedDomainsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) PageSize ¶
added in v0.168.0
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsAuthorizedDomainsListCall

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) PageToken ¶
added in v0.168.0
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsAuthorizedDomainsListCall

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) Pages ¶
added in v0.168.0
func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Pages(ctx context.Context, f func(*ListAuthorizedDomainsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApplicationsAuthorizedDomainsService ¶
added in v0.168.0
type ProjectsLocationsApplicationsAuthorizedDomainsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsAuthorizedDomainsService ¶
added in v0.168.0
func NewProjectsLocationsApplicationsAuthorizedDomainsService(s *APIService) *ProjectsLocationsApplicationsAuthorizedDomainsService
func (*ProjectsLocationsApplicationsAuthorizedDomainsService) List ¶
added in v0.168.0
func (r *ProjectsLocationsApplicationsAuthorizedDomainsService) List(projectsId string, locationsId string, applicationsId string) *ProjectsLocationsApplicationsAuthorizedDomainsListCall

List: Lists all domains the user is authorized to administer.

applicationsId: Part of `parent`. See documentation of `projectsId`.
locationsId: Part of `parent`. See documentation of `projectsId`.
projectsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
type ProjectsLocationsApplicationsDomainMappingsCreateCall ¶
added in v0.239.0
type ProjectsLocationsApplicationsDomainMappingsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsDomainMappingsCreateCall) Context ¶
added in v0.239.0
func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsDomainMappingsCreateCall) Do ¶
added in v0.239.0
func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.applications.domainMappings.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsDomainMappingsCreateCall) Fields ¶
added in v0.239.0
func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsDomainMappingsCreateCall) Header ¶
added in v0.239.0
func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsDomainMappingsCreateCall) OverrideStrategy ¶
added in v0.239.0
func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) OverrideStrategy(overrideStrategy string) *ProjectsLocationsApplicationsDomainMappingsCreateCall

OverrideStrategy sets the optional parameter "overrideStrategy": Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected.

Possible values:

"UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY" - Strategy unspecified. Defaults to


STRICT.

"STRICT" - Overrides not allowed. If a mapping already exists for the


specified domain, the request will return an ALREADY_EXISTS (409).

"OVERRIDE" - Overrides allowed. If a mapping already exists for the


specified domain, the request will overwrite it. Note that this might stop another Google product from serving. For example, if the domain is mapped to another App Engine application, that app will no longer serve from that domain.

type ProjectsLocationsApplicationsDomainMappingsDeleteCall ¶
added in v0.252.0
type ProjectsLocationsApplicationsDomainMappingsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsDomainMappingsDeleteCall) Context ¶
added in v0.252.0
func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsDomainMappingsDeleteCall) Do ¶
added in v0.252.0
func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.applications.domainMappings.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsDomainMappingsDeleteCall) Fields ¶
added in v0.252.0
func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsDomainMappingsDeleteCall) Header ¶
added in v0.252.0
func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsDomainMappingsGetCall ¶
added in v0.234.0
type ProjectsLocationsApplicationsDomainMappingsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsDomainMappingsGetCall) Context ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsDomainMappingsGetCall) Do ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Do(opts ...googleapi.CallOption) (*DomainMapping, error)

Do executes the "appengine.projects.locations.applications.domainMappings.get" call. Any non-2xx status code is an error. Response headers are in either *DomainMapping.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsDomainMappingsGetCall) Fields ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsDomainMappingsGetCall) Header ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsDomainMappingsGetCall) IfNoneMatch ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsDomainMappingsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApplicationsDomainMappingsListCall ¶
added in v0.256.0
type ProjectsLocationsApplicationsDomainMappingsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsDomainMappingsListCall) Context ¶
added in v0.256.0
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsDomainMappingsListCall) Do ¶
added in v0.256.0
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Do(opts ...googleapi.CallOption) (*ListDomainMappingsResponse, error)

Do executes the "appengine.projects.locations.applications.domainMappings.list" call. Any non-2xx status code is an error. Response headers are in either *ListDomainMappingsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsDomainMappingsListCall) Fields ¶
added in v0.256.0
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsDomainMappingsListCall) Header ¶
added in v0.256.0
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsDomainMappingsListCall) IfNoneMatch ¶
added in v0.256.0
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsDomainMappingsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApplicationsDomainMappingsListCall) PageSize ¶
added in v0.256.0
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsDomainMappingsListCall

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

func (*ProjectsLocationsApplicationsDomainMappingsListCall) PageToken ¶
added in v0.256.0
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsDomainMappingsListCall

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

func (*ProjectsLocationsApplicationsDomainMappingsListCall) Pages ¶
added in v0.256.0
func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Pages(ctx context.Context, f func(*ListDomainMappingsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApplicationsDomainMappingsPatchCall ¶
added in v0.252.0
type ProjectsLocationsApplicationsDomainMappingsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsDomainMappingsPatchCall) Context ¶
added in v0.252.0
func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsDomainMappingsPatchCall) Do ¶
added in v0.252.0
func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.applications.domainMappings.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsDomainMappingsPatchCall) Fields ¶
added in v0.252.0
func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsDomainMappingsPatchCall) Header ¶
added in v0.252.0
func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsDomainMappingsPatchCall) UpdateMask ¶
added in v0.252.0
func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsDomainMappingsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Standard field mask for the set of fields to be updated.

type ProjectsLocationsApplicationsDomainMappingsService ¶
added in v0.234.0
type ProjectsLocationsApplicationsDomainMappingsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsDomainMappingsService ¶
added in v0.234.0
func NewProjectsLocationsApplicationsDomainMappingsService(s *APIService) *ProjectsLocationsApplicationsDomainMappingsService
func (*ProjectsLocationsApplicationsDomainMappingsService) Create ¶
added in v0.239.0
func (r *ProjectsLocationsApplicationsDomainMappingsService) Create(projectsId string, locationsId string, applicationsId string, domainmapping *DomainMapping) *ProjectsLocationsApplicationsDomainMappingsCreateCall

Create: Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see AuthorizedDomains.ListAuthorizedDomains.

applicationsId: Part of `parent`. See documentation of `projectsId`.
locationsId: Part of `parent`. See documentation of `projectsId`.
projectsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
func (*ProjectsLocationsApplicationsDomainMappingsService) Delete ¶
added in v0.252.0
func (r *ProjectsLocationsApplicationsDomainMappingsService) Delete(projectsId string, locationsId string, applicationsId string, domainMappingsId string) *ProjectsLocationsApplicationsDomainMappingsDeleteCall

Delete: Deletes the specified domain mapping. A user must be authorized to administer the associated domain in order to delete a DomainMapping resource.

applicationsId: Part of `name`. See documentation of `projectsId`.
domainMappingsId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource to delete. Example: apps/myapp/domainMappings/example.com.
func (*ProjectsLocationsApplicationsDomainMappingsService) Get ¶
added in v0.234.0
func (r *ProjectsLocationsApplicationsDomainMappingsService) Get(projectsId string, locationsId string, applicationsId string, domainMappingsId string) *ProjectsLocationsApplicationsDomainMappingsGetCall

Get: Gets the specified domain mapping.

applicationsId: Part of `name`. See documentation of `projectsId`.
domainMappingsId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource requested. Example: apps/myapp/domainMappings/example.com.
func (*ProjectsLocationsApplicationsDomainMappingsService) List ¶
added in v0.256.0
func (r *ProjectsLocationsApplicationsDomainMappingsService) List(projectsId string, locationsId string, applicationsId string) *ProjectsLocationsApplicationsDomainMappingsListCall

List: Lists the domain mappings on an application.

applicationsId: Part of `parent`. See documentation of `projectsId`.
locationsId: Part of `parent`. See documentation of `projectsId`.
projectsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.
func (*ProjectsLocationsApplicationsDomainMappingsService) Patch ¶
added in v0.252.0
func (r *ProjectsLocationsApplicationsDomainMappingsService) Patch(projectsId string, locationsId string, applicationsId string, domainMappingsId string, domainmapping *DomainMapping) *ProjectsLocationsApplicationsDomainMappingsPatchCall

Patch: Updates the specified domain mapping. To map an SSL certificate to a domain mapping, update certificate_id to point to an AuthorizedCertificate resource. A user must be authorized to administer the associated domain in order to update a DomainMapping resource.

applicationsId: Part of `name`. See documentation of `projectsId`.
domainMappingsId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource to update. Example: apps/myapp/domainMappings/example.com.
type ProjectsLocationsApplicationsPatchCall ¶
added in v0.227.0
type ProjectsLocationsApplicationsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsPatchCall) Context ¶
added in v0.227.0
func (c *ProjectsLocationsApplicationsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsPatchCall) Do ¶
added in v0.227.0
func (c *ProjectsLocationsApplicationsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.applications.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsPatchCall) Fields ¶
added in v0.227.0
func (c *ProjectsLocationsApplicationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsPatchCall) Header ¶
added in v0.227.0
func (c *ProjectsLocationsApplicationsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsPatchCall) UpdateMask ¶
added in v0.227.0
func (c *ProjectsLocationsApplicationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Standard field mask for the set of fields to be updated.

type ProjectsLocationsApplicationsService ¶
added in v0.101.0
type ProjectsLocationsApplicationsService struct {
	AuthorizedCertificates *ProjectsLocationsApplicationsAuthorizedCertificatesService

	AuthorizedDomains *ProjectsLocationsApplicationsAuthorizedDomainsService

	DomainMappings *ProjectsLocationsApplicationsDomainMappingsService

	Services *ProjectsLocationsApplicationsServicesService
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsService ¶
added in v0.101.0
func NewProjectsLocationsApplicationsService(s *APIService) *ProjectsLocationsApplicationsService
func (*ProjectsLocationsApplicationsService) Patch ¶
added in v0.227.0
func (r *ProjectsLocationsApplicationsService) Patch(projectsId string, locationsId string, applicationsId string, application *Application) *ProjectsLocationsApplicationsPatchCall

Patch: Updates the specified Application resource. You can update the following fields: auth_domain - Google authentication domain for controlling user access to the application. default_cookie_expiration - Cookie expiration policy for the application. iap - Identity-Aware Proxy properties for the application.

applicationsId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the Application resource to update. Example: apps/myapp.
type ProjectsLocationsApplicationsServicesDeleteCall ¶
added in v0.211.0
type ProjectsLocationsApplicationsServicesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesDeleteCall) Context ¶
added in v0.211.0
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesDeleteCall) Do ¶
added in v0.211.0
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.applications.services.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesDeleteCall) Fields ¶
added in v0.211.0
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesDeleteCall) Header ¶
added in v0.211.0
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsServicesPatchCall ¶
added in v0.234.0
type ProjectsLocationsApplicationsServicesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesPatchCall) Context ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsServicesPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesPatchCall) Do ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsServicesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.applications.services.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesPatchCall) Fields ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsServicesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesPatchCall) Header ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsServicesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsServicesPatchCall) MigrateTraffic ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsServicesPatchCall) MigrateTraffic(migrateTraffic bool) *ProjectsLocationsApplicationsServicesPatchCall

MigrateTraffic sets the optional parameter "migrateTraffic": Set to true to gradually shift traffic to one or more versions that you specify. By default, traffic is shifted immediately. For gradual traffic migration, the target versions must be located within instances that are configured for both warmup requests (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#InboundServiceType) and automatic scaling (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#AutomaticScaling). You must specify the shardBy (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services#ShardBy) field in the Service resource. Gradual traffic migration is not supported in the App Engine flexible environment. For examples, see Migrating and Splitting Traffic (https://cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic).

func (*ProjectsLocationsApplicationsServicesPatchCall) UpdateMask ¶
added in v0.234.0
func (c *ProjectsLocationsApplicationsServicesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsServicesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Standard field mask for the set of fields to be updated.

type ProjectsLocationsApplicationsServicesService ¶
added in v0.127.0
type ProjectsLocationsApplicationsServicesService struct {
	Versions *ProjectsLocationsApplicationsServicesVersionsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsServicesService ¶
added in v0.127.0
func NewProjectsLocationsApplicationsServicesService(s *APIService) *ProjectsLocationsApplicationsServicesService
func (*ProjectsLocationsApplicationsServicesService) Delete ¶
added in v0.211.0
func (r *ProjectsLocationsApplicationsServicesService) Delete(projectsId string, locationsId string, applicationsId string, servicesId string) *ProjectsLocationsApplicationsServicesDeleteCall

Delete: Deletes the specified service and all enclosed versions.

applicationsId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default.
servicesId: Part of `name`. See documentation of `projectsId`.
func (*ProjectsLocationsApplicationsServicesService) Patch ¶
added in v0.234.0
func (r *ProjectsLocationsApplicationsServicesService) Patch(projectsId string, locationsId string, applicationsId string, servicesId string, service *Service) *ProjectsLocationsApplicationsServicesPatchCall

Patch: Updates the configuration of the specified service.

applicationsId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource to update. Example: apps/myapp/services/default.
servicesId: Part of `name`. See documentation of `projectsId`.
type ProjectsLocationsApplicationsServicesVersionsDeleteCall ¶
added in v0.201.0
type ProjectsLocationsApplicationsServicesVersionsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesVersionsDeleteCall) Context ¶
added in v0.201.0
func (c *ProjectsLocationsApplicationsServicesVersionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesVersionsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesVersionsDeleteCall) Do ¶
added in v0.201.0
func (c *ProjectsLocationsApplicationsServicesVersionsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.applications.services.versions.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesVersionsDeleteCall) Fields ¶
added in v0.201.0
func (c *ProjectsLocationsApplicationsServicesVersionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesVersionsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesVersionsDeleteCall) Header ¶
added in v0.201.0
func (c *ProjectsLocationsApplicationsServicesVersionsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall ¶
added in v0.261.0
type ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Context ¶
added in v0.261.0
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Do ¶
added in v0.261.0
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.applications.services.versions.instances.debug" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Fields ¶
added in v0.261.0
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Header ¶
added in v0.261.0
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall ¶
added in v0.266.0
type ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Context ¶
added in v0.266.0
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Do ¶
added in v0.266.0
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.applications.services.versions.instances.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Fields ¶
added in v0.266.0
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Header ¶
added in v0.266.0
func (c *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsServicesVersionsInstancesService ¶
added in v0.261.0
type ProjectsLocationsApplicationsServicesVersionsInstancesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsServicesVersionsInstancesService ¶
added in v0.261.0
func NewProjectsLocationsApplicationsServicesVersionsInstancesService(s *APIService) *ProjectsLocationsApplicationsServicesVersionsInstancesService
func (*ProjectsLocationsApplicationsServicesVersionsInstancesService) Debug ¶
added in v0.261.0
func (r *ProjectsLocationsApplicationsServicesVersionsInstancesService) Debug(projectsId string, locationsId string, applicationsId string, servicesId string, versionsId string, instancesId string, debuginstancerequest *DebugInstanceRequest) *ProjectsLocationsApplicationsServicesVersionsInstancesDebugCall

Debug: Enables debugging on a VM instance. This allows you to use the SSH command to connect to the virtual machine where the instance lives. While in "debug mode", the instance continues to serve live traffic. You should delete the instance when you are done debugging and then allow the system to take over and determine if another instance should be started.Only applicable for instances in App Engine flexible environment.

applicationsId: Part of `name`. See documentation of `projectsId`.
instancesId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default/versions/v1/instances/instance-1.
servicesId: Part of `name`. See documentation of `projectsId`.
versionsId: Part of `name`. See documentation of `projectsId`.
func (*ProjectsLocationsApplicationsServicesVersionsInstancesService) Delete ¶
added in v0.266.0
func (r *ProjectsLocationsApplicationsServicesVersionsInstancesService) Delete(projectsId string, locationsId string, applicationsId string, servicesId string, versionsId string, instancesId string) *ProjectsLocationsApplicationsServicesVersionsInstancesDeleteCall

Delete: Stops a running instance.The instance might be automatically recreated based on the scaling settings of the version. For more information, see "How Instances are Managed" (standard environment (https://cloud.google.com/appengine/docs/standard/python/how-instances-are-managed) | flexible environment (https://cloud.google.com/appengine/docs/flexible/python/how-instances-are-managed)).To ensure that instances are not re-created and avoid getting billed, you can stop all instances within the target version by changing the serving status of the version to STOPPED with the apps.services.versions.patch (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/patch) method.

applicationsId: Part of `name`. See documentation of `projectsId`.
instancesId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default/versions/v1/instances/instance-1.
servicesId: Part of `name`. See documentation of `projectsId`.
versionsId: Part of `name`. See documentation of `projectsId`.
type ProjectsLocationsApplicationsServicesVersionsPatchCall ¶
added in v0.230.0
type ProjectsLocationsApplicationsServicesVersionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesVersionsPatchCall) Context ¶
added in v0.230.0
func (c *ProjectsLocationsApplicationsServicesVersionsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesVersionsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesVersionsPatchCall) Do ¶
added in v0.230.0
func (c *ProjectsLocationsApplicationsServicesVersionsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.applications.services.versions.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesVersionsPatchCall) Fields ¶
added in v0.230.0
func (c *ProjectsLocationsApplicationsServicesVersionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesVersionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesVersionsPatchCall) Header ¶
added in v0.230.0
func (c *ProjectsLocationsApplicationsServicesVersionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsServicesVersionsPatchCall) UpdateMask ¶
added in v0.230.0
func (c *ProjectsLocationsApplicationsServicesVersionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsServicesVersionsPatchCall

UpdateMask sets the optional parameter "updateMask": Standard field mask for the set of fields to be updated.

type ProjectsLocationsApplicationsServicesVersionsService ¶
added in v0.201.0
type ProjectsLocationsApplicationsServicesVersionsService struct {
	Instances *ProjectsLocationsApplicationsServicesVersionsInstancesService
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsServicesVersionsService ¶
added in v0.201.0
func NewProjectsLocationsApplicationsServicesVersionsService(s *APIService) *ProjectsLocationsApplicationsServicesVersionsService
func (*ProjectsLocationsApplicationsServicesVersionsService) Delete ¶
added in v0.201.0
func (r *ProjectsLocationsApplicationsServicesVersionsService) Delete(projectsId string, locationsId string, applicationsId string, servicesId string, versionsId string) *ProjectsLocationsApplicationsServicesVersionsDeleteCall

Delete: Deletes an existing Version resource.

applicationsId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource requested. Example: apps/myapp/services/default/versions/v1.
servicesId: Part of `name`. See documentation of `projectsId`.
versionsId: Part of `name`. See documentation of `projectsId`.
func (*ProjectsLocationsApplicationsServicesVersionsService) Patch ¶
added in v0.230.0
func (r *ProjectsLocationsApplicationsServicesVersionsService) Patch(projectsId string, locationsId string, applicationsId string, servicesId string, versionsId string, version *Version) *ProjectsLocationsApplicationsServicesVersionsPatchCall

Patch: Updates the specified Version resource. You can specify the following fields depending on the App Engine environment and type of scaling that the version resource uses:Standard environment instance_class (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.instance_class)automatic scaling in the standard environment: automatic_scaling.min_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.max_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling) automaticScaling.standard_scheduler_settings.max_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.min_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.target_cpu_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.target_throughput_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#StandardSchedulerSettings)basic scaling or manual scaling in the standard environment: serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.serving_status) manual_scaling.instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#manualscaling)Flexible environment serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.serving_status)automatic scaling in the flexible environment: automatic_scaling.min_total_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.max_total_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.cool_down_period_sec (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.cpu_utilization.target_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#Version.FIELDS.automatic_scaling)manual scaling in the flexible environment: manual_scaling.instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#manualscaling)

applicationsId: Part of `name`. See documentation of `projectsId`.
locationsId: Part of `name`. See documentation of `projectsId`.
projectsId: Part of `name`. Name of the resource to update. Example: apps/myapp/services/default/versions/1.
servicesId: Part of `name`. See documentation of `projectsId`.
versionsId: Part of `name`. See documentation of `projectsId`.
type ProjectsLocationsGetCall ¶
added in v0.101.0
type ProjectsLocationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetCall) Context ¶
added in v0.101.0
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetCall) Do ¶
added in v0.101.0
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)

Do executes the "appengine.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetCall) Fields ¶
added in v0.101.0
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetCall) Header ¶
added in v0.101.0
func (c *ProjectsLocationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetCall) IfNoneMatch ¶
added in v0.101.0
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsListCall ¶
added in v0.101.0
type ProjectsLocationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsListCall) Context ¶
added in v0.101.0
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsListCall) Do ¶
added in v0.101.0
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)

Do executes the "appengine.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsListCall) ExtraLocationTypes ¶
added in v0.230.0
func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

func (*ProjectsLocationsListCall) Fields ¶
added in v0.101.0
func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsListCall) Filter ¶
added in v0.101.0
func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 (https://google.aip.dev/160).

func (*ProjectsLocationsListCall) Header ¶
added in v0.101.0
func (c *ProjectsLocationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsListCall) IfNoneMatch ¶
added in v0.101.0
func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsListCall) PageSize ¶
added in v0.101.0
func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

func (*ProjectsLocationsListCall) PageToken ¶
added in v0.101.0
func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall

PageToken sets the optional parameter "pageToken": A page token received from the next_page_token field in the response. Send that page token to receive the subsequent page.

func (*ProjectsLocationsListCall) Pages ¶
added in v0.101.0
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsOperationsGetCall ¶
added in v0.101.0
type ProjectsLocationsOperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsGetCall) Context ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsGetCall) Do ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "appengine.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsGetCall) Fields ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsGetCall) Header ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsOperationsGetCall) IfNoneMatch ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOperationsListCall ¶
added in v0.101.0
type ProjectsLocationsOperationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsListCall) Context ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsOperationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsListCall) Do ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)

Do executes the "appengine.projects.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsListCall) Fields ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsListCall) Filter ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsListCall) Filter(filter string) *ProjectsLocationsOperationsListCall

Filter sets the optional parameter "filter": The standard list filter.

func (*ProjectsLocationsOperationsListCall) Header ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsOperationsListCall) IfNoneMatch ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsOperationsListCall) PageSize ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsOperationsListCall

PageSize sets the optional parameter "pageSize": The standard list page size.

func (*ProjectsLocationsOperationsListCall) PageToken ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsOperationsListCall

PageToken sets the optional parameter "pageToken": The standard list page token.

func (*ProjectsLocationsOperationsListCall) Pages ¶
added in v0.101.0
func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsOperationsListCall) ReturnPartialSuccess ¶
added in v0.252.0
func (c *ProjectsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *ProjectsLocationsOperationsListCall

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to true, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field.This can only be true when reading across collections. For example, when parent is set to "projects/example/locations/-".This field is not supported by default and will result in an UNIMPLEMENTED error if set unless explicitly documented otherwise in service or product specific documentation.

type ProjectsLocationsOperationsService ¶
added in v0.101.0
type ProjectsLocationsOperationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsOperationsService ¶
added in v0.101.0
func NewProjectsLocationsOperationsService(s *APIService) *ProjectsLocationsOperationsService
func (*ProjectsLocationsOperationsService) Get ¶
added in v0.101.0
func (r *ProjectsLocationsOperationsService) Get(projectsId string, locationsId string, operationsId string) *ProjectsLocationsOperationsGetCall

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- locationsId: Part of `name`. See documentation of `projectsId`. - operationsId: Part of `name`. See documentation of `projectsId`. - projectsId: Part of `name`. The name of the operation resource.

func (*ProjectsLocationsOperationsService) List ¶
added in v0.101.0
func (r *ProjectsLocationsOperationsService) List(projectsId string, locationsId string) *ProjectsLocationsOperationsListCall

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.

- locationsId: Part of `name`. See documentation of `projectsId`. - projectsId: Part of `name`. The name of the operation's parent resource.

type ProjectsLocationsService ¶
added in v0.101.0
type ProjectsLocationsService struct {
	Applications *ProjectsLocationsApplicationsService

	Operations *ProjectsLocationsOperationsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsService ¶
added in v0.101.0
func NewProjectsLocationsService(s *APIService) *ProjectsLocationsService
func (*ProjectsLocationsService) Get ¶
added in v0.101.0
func (r *ProjectsLocationsService) Get(projectsId string, locationsId string) *ProjectsLocationsGetCall

Get: Gets information about a location.

- locationsId: Part of `name`. See documentation of `projectsId`. - projectsId: Part of `name`. Resource name for the location.

func (*ProjectsLocationsService) List ¶
added in v0.101.0
func (r *ProjectsLocationsService) List(projectsId string) *ProjectsLocationsListCall

List: Lists information about the supported locations for this service. This method can be called in two ways: List all public locations: Use the path GET /v1/locations. List project-visible locations: Use the path GET /v1/projects/{project_id}/locations. This may include public locations as well as private or other locations specifically visible to the project.

projectsId: Part of `name`. The resource that owns the locations collection, if applicable.
type ProjectsMetadata ¶
added in v0.105.0
type ProjectsMetadata struct {
	// ConsumerProjectId: The consumer project id.
	ConsumerProjectId string `json:"consumerProjectId,omitempty"`
	// ConsumerProjectNumber: The consumer project number.
	ConsumerProjectNumber int64 `json:"consumerProjectNumber,omitempty,string"`
	// ConsumerProjectState: The CCFE state of the consumer project. It is the same
	// state that is communicated to the CLH during project events. Notice that
	// this field is not set in the DB, it is only set in this proto when
	// communicated to CLH in the side channel.
	//
	// Possible values:
	//   "UNKNOWN_STATE" - A container should never be in an unknown state. Receipt
	// of a container with this state is an error.
	//   "ON" - CCFE considers the container to be serving or transitioning into
	// serving.
	//   "OFF" - CCFE considers the container to be in an OFF state. This could
	// occur due to various factors. The state could be triggered by
	// Google-internal audits (ex. abuse suspension, billing closed) or cleanups
	// trigged by compliance systems (ex. data governance hide). User-initiated
	// events such as service management deactivation trigger a container to an OFF
	// state.CLHs might choose to do nothing in this case or to turn off costly
	// resources. CLHs need to consider the customer experience if an ON/OFF/ON
	// sequence of state transitions occurs vs. the cost of deleting resources,
	// keeping metadata about resources, or even keeping resources live for a
	// period of time.CCFE will not send any new customer requests to the CLH when
	// the container is in an OFF state. However, CCFE will allow all previous
	// customer requests relayed to CLH to complete.
	//   "DELETED" - This state indicates that the container has been (or is being)
	// completely removed. This is often due to a data governance purge request and
	// therefore resources should be deleted when this state is reached.
	ConsumerProjectState string `json:"consumerProjectState,omitempty"`
	// GceTag: The GCE tags associated with the consumer project and those
	// inherited due to their ancestry, if any. Not supported by CCFE.
	GceTag []*GceTag `json:"gceTag,omitempty"`
	// IsGceProjectDeprovisioning: DEPRECATED: Indicates whether the GCE project is
	// in the DEPROVISIONING state. This field is a temporary workaround (see
	// b/475310865) to allow GCE extensions to bypass certain checks during
	// deprovisioning. It will be replaced by a permanent solution in the future.
	IsGceProjectDeprovisioning bool `json:"isGceProjectDeprovisioning,omitempty"`
	// P4ServiceAccount: The service account authorized to operate on the consumer
	// project. Note: CCFE only propagates P4SA with default tag to CLH.
	P4ServiceAccount string `json:"p4ServiceAccount,omitempty"`
	// ProducerProjectId: The producer project id.
	ProducerProjectId string `json:"producerProjectId,omitempty"`
	// ProducerProjectNumber: The producer project number.
	ProducerProjectNumber int64 `json:"producerProjectNumber,omitempty,string"`
	// TenantProjectId: The tenant project id.
	TenantProjectId string `json:"tenantProjectId,omitempty"`
	// TenantProjectNumber: The tenant project number.
	TenantProjectNumber int64 `json:"tenantProjectNumber,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "ConsumerProjectId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConsumerProjectId") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProjectsMetadata: ProjectsMetadata is the metadata CCFE stores about the all the relevant projects (tenant, consumer, producer).

func (ProjectsMetadata) MarshalJSON ¶
added in v0.105.0
func (s ProjectsMetadata) MarshalJSON() ([]byte, error)
type ProjectsService ¶
added in v0.101.0
type ProjectsService struct {
	Locations *ProjectsLocationsService
	// contains filtered or unexported fields
}
func NewProjectsService ¶
added in v0.101.0
func NewProjectsService(s *APIService) *ProjectsService
type ReadinessCheck ¶
type ReadinessCheck struct {
	// AppStartTimeout: A maximum time limit on application initialization,
	// measured from moment the application successfully replies to a healthcheck
	// until it is ready to serve traffic.
	AppStartTimeout string `json:"appStartTimeout,omitempty"`
	// CheckInterval: Interval between health checks.
	CheckInterval string `json:"checkInterval,omitempty"`
	// FailureThreshold: Number of consecutive failed checks required before
	// removing traffic.
	FailureThreshold int64 `json:"failureThreshold,omitempty"`
	// Host: Host header to send when performing a HTTP Readiness check. Example:
	// "myapp.appspot.com"
	Host string `json:"host,omitempty"`
	// Path: The request path.
	Path string `json:"path,omitempty"`
	// SuccessThreshold: Number of consecutive successful checks required before
	// receiving traffic.
	SuccessThreshold int64 `json:"successThreshold,omitempty"`
	// Timeout: Time before the check is considered failed.
	Timeout string `json:"timeout,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AppStartTimeout") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppStartTimeout") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReadinessCheck: Readiness checking configuration for VM instances. Unhealthy instances are removed from traffic rotation.

func (ReadinessCheck) MarshalJSON ¶
func (s ReadinessCheck) MarshalJSON() ([]byte, error)
type Reasons ¶
added in v0.105.0
type Reasons struct {
	// Possible values:
	//   "ABUSE_UNKNOWN_REASON" - An unknown reason indicates that the abuse system
	// has not sent a signal for this container.
	//   "ABUSE_CONTROL_PLANE_SYNC" - Due to various reasons CCFE might proactively
	// restate a container state to a CLH to ensure that the CLH and CCFE are both
	// aware of the container state. This reason can be tied to any of the states.
	//   "SUSPEND" - If a container is deemed abusive we receive a suspend signal.
	// Suspend is a reason to put the container into an INTERNAL_OFF state.
	//   "REINSTATE" - Containers that were once considered abusive can later be
	// deemed non-abusive. When this happens we must reinstate the container.
	// Reinstate is a reason to put the container into an ON state.
	Abuse string `json:"abuse,omitempty"`
	// Possible values:
	//   "BILLING_UNKNOWN_REASON" - An unknown reason indicates that the billing
	// system has not sent a signal for this container.
	//   "BILLING_CONTROL_PLANE_SYNC" - Due to various reasons CCFE might
	// proactively restate a container state to a CLH to ensure that the CLH and
	// CCFE are both aware of the container state. This reason can be tied to any
	// of the states.
	//   "PROBATION" - Minor infractions cause a probation signal to be sent.
	// Probation is a reason to put the container into a ON state even though it is
	// a negative signal. CCFE will block mutations for this container while it is
	// on billing probation, but the CLH is expected to serve non-mutation
	// requests.
	//   "CLOSE" - When a billing account is closed, it is a stronger signal about
	// non-payment. Close is a reason to put the container into an INTERNAL_OFF
	// state.
	//   "OPEN" - Consumers can re-open billing accounts and update accounts to
	// pull them out of probation. When this happens, we get a signal that the
	// account is open. Open is a reason to put the container into an ON state.
	Billing string `json:"billing,omitempty"`
	// Possible values:
	//   "DATA_GOVERNANCE_UNKNOWN_REASON" - An unknown reason indicates that data
	// governance has not sent a signal for this container.
	//   "DATA_GOVERNANCE_CONTROL_PLANE_SYNC" - Due to various reasons CCFE might
	// proactively restate a container state to a CLH to ensure that the CLH and
	// CCFE are both aware of the container state. This reason can be tied to any
	// of the states.
	//   "HIDE" - When a container is deleted we retain some data for a period of
	// time to allow the consumer to change their mind. Data governance sends a
	// signal to hide the data when this occurs. Hide is a reason to put the
	// container in an INTERNAL_OFF state.
	//   "UNHIDE" - The decision to un-delete a container can be made. When this
	// happens data governance tells us to unhide any hidden data. Unhide is a
	// reason to put the container in an ON state.
	//   "PURGE" - After a period of time data must be completely removed from our
	// systems. When data governance sends a purge signal we need to remove data.
	// Purge is a reason to put the container in a DELETED state. Purge is the only
	// event that triggers a delete mutation. All other events have update
	// semantics.
	DataGovernance string `json:"dataGovernance,omitempty"`
	// ServiceActivation: Consumer Container denotes if the service is active
	// within a project or not. This information could be used to clean up
	// resources in case service in DISABLED_FULL i.e. Service is inactive > 30
	// days.
	//
	// Possible values:
	//   "SERVICE_ACTIVATION_STATUS_UNSPECIFIED" - Default Unspecified status
	//   "SERVICE_ACTIVATION_ENABLED" - Service is active in the project.
	//   "SERVICE_ACTIVATION_DISABLED" - Service is disabled in the project
	// recently i.e., within last 24 hours.
	//   "SERVICE_ACTIVATION_DISABLED_FULL" - Service has been disabled for
	// configured grace_period (default 30 days).
	//   "SERVICE_ACTIVATION_UNKNOWN_REASON" - Happens when PSM cannot determine
	// the status of service in a project Could happen due to variety of reasons
	// like PERMISSION_DENIED or Project got deleted etc.
	ServiceActivation string `json:"serviceActivation,omitempty"`
	// Possible values:
	//   "SERVICE_MANAGEMENT_UNKNOWN_REASON" - An unknown reason indicates that we
	// have not received a signal from service management about this container.
	// Since containers are created by request of service management, this reason
	// should never be set.
	//   "SERVICE_MANAGEMENT_CONTROL_PLANE_SYNC" - Due to various reasons CCFE
	// might proactively restate a container state to a CLH to ensure that the CLH
	// and CCFE are both aware of the container state. This reason can be tied to
	// any of the states.
	//   "ACTIVATION" - When a customer activates an API CCFE notifies the CLH and
	// sets the container to the ON state.
	//   "PREPARE_DEACTIVATION" - When a customer deactivates and API service
	// management starts a two-step process to perform the deactivation. The first
	// step is to prepare. Prepare is a reason to put the container in a
	// EXTERNAL_OFF state.
	//   "ABORT_DEACTIVATION" - If the deactivation is cancelled, service managed
	// needs to abort the deactivation. Abort is a reason to put the container in
	// an ON state.
	//   "COMMIT_DEACTIVATION" - If the deactivation is followed through with,
	// service management needs to finish deactivation. Commit is a reason to put
	// the container in a DELETED state.
	ServiceManagement string `json:"serviceManagement,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Abuse") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Abuse") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Reasons: Containers transition between and within states based on reasons sent from various systems. CCFE will provide the CLH with reasons for the current state per system.The current systems that CCFE supports are: Service Management (Inception) Data Governance (Wipeout) Abuse (Ares) Billing (Internal Cloud Billing API) Service Activation (Service Controller)

func (Reasons) MarshalJSON ¶
added in v0.105.0
func (s Reasons) MarshalJSON() ([]byte, error)
type RepairApplicationRequest ¶
type RepairApplicationRequest struct {
}

RepairApplicationRequest: Request message for 'Applications.RepairApplication'.

type RequestUtilization ¶
type RequestUtilization struct {
	// TargetConcurrentRequests: Target number of concurrent requests.
	TargetConcurrentRequests int64 `json:"targetConcurrentRequests,omitempty"`
	// TargetRequestCountPerSecond: Target requests per second.
	TargetRequestCountPerSecond int64 `json:"targetRequestCountPerSecond,omitempty"`
	// ForceSendFields is a list of field names (e.g. "TargetConcurrentRequests")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "TargetConcurrentRequests") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RequestUtilization: Target scaling by request utilization. Only applicable in the App Engine flexible environment.

func (RequestUtilization) MarshalJSON ¶
func (s RequestUtilization) MarshalJSON() ([]byte, error)
type ResourceEvent ¶
added in v0.210.0
type ResourceEvent struct {
	// EventId: The unique ID for this per-resource event. CLHs can use this value
	// to dedup repeated calls. required
	EventId string `json:"eventId,omitempty"`
	// Name: The name of the resource for which this event is. required
	Name string `json:"name,omitempty"`
	// State: The state of the project that led to this event.
	State *ContainerState `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EventId") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ResourceEvent: The request that is passed to CLH during per-resource events. The request will be sent with update semantics in all cases except for data governance purge events. These events will be sent with delete semantics and the CLH is expected to delete the resource receiving this event.

func (ResourceEvent) MarshalJSON ¶
added in v0.210.0
func (s ResourceEvent) MarshalJSON() ([]byte, error)
type ResourceRecord ¶
type ResourceRecord struct {
	// Name: Relative name of the object affected by this record. Only applicable
	// for CNAME records. Example: 'www'.
	Name string `json:"name,omitempty"`
	// Rrdata: Data for this record. Values vary by record type, as defined in RFC
	// 1035 (section 5) and RFC 1034 (section 3.6.1).
	Rrdata string `json:"rrdata,omitempty"`
	// Type: Resource record type. Example: AAAA.
	//
	// Possible values:
	//   "A" - An A resource record. Data is an IPv4 address.
	//   "AAAA" - An AAAA resource record. Data is an IPv6 address.
	//   "CNAME" - A CNAME resource record. Data is a domain name to be aliased.
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

ResourceRecord: A DNS resource record.

func (ResourceRecord) MarshalJSON ¶
func (s ResourceRecord) MarshalJSON() ([]byte, error)
type Resources ¶
type Resources struct {
	// Cpu: Number of CPU cores needed.
	Cpu float64 `json:"cpu,omitempty"`
	// DiskGb: Disk size (GB) needed.
	DiskGb float64 `json:"diskGb,omitempty"`
	// KmsKeyReference: The name of the encryption key that is stored in Google
	// Cloud KMS. Only should be used by Cloud Composer to encrypt the vm disk
	KmsKeyReference string `json:"kmsKeyReference,omitempty"`
	// MemoryGb: Memory (GB) needed.
	MemoryGb float64 `json:"memoryGb,omitempty"`
	// Volumes: User specified volumes.
	Volumes []*Volume `json:"volumes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Cpu") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Cpu") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Resources: Machine resources for a version.

func (Resources) MarshalJSON ¶
func (s Resources) MarshalJSON() ([]byte, error)
func (*Resources) UnmarshalJSON ¶
func (s *Resources) UnmarshalJSON(data []byte) error
type Runtime ¶
added in v0.137.0
type Runtime struct {
	// DecommissionedDate: Date when Runtime is decommissioned.
	DecommissionedDate *Date `json:"decommissionedDate,omitempty"`
	// DeprecationDate: Date when Runtime is deprecated.
	DeprecationDate *Date `json:"deprecationDate,omitempty"`
	// DisplayName: User-friendly display name, e.g. 'Node.js 12', etc.
	DisplayName string `json:"displayName,omitempty"`
	// EndOfSupportDate: Date when Runtime is end of support.
	EndOfSupportDate *Date `json:"endOfSupportDate,omitempty"`
	// Environment: The environment of the runtime.
	//
	// Possible values:
	//   "ENVIRONMENT_UNSPECIFIED" - Default value.
	//   "STANDARD" - App Engine Standard.
	//   "FLEXIBLE" - App Engine Flexible
	Environment string `json:"environment,omitempty"`
	// Name: The name of the runtime, e.g., 'go113', 'nodejs12', etc.
	Name string `json:"name,omitempty"`
	// Stage: The stage of life this runtime is in, e.g., BETA, GA, etc.
	//
	// Possible values:
	//   "RUNTIME_STAGE_UNSPECIFIED" - Not specified.
	//   "DEVELOPMENT" - The runtime is in development.
	//   "ALPHA" - The runtime is in the Alpha stage.
	//   "BETA" - The runtime is in the Beta stage.
	//   "GA" - The runtime is generally available.
	//   "DEPRECATED" - The runtime is deprecated.
	//   "DECOMMISSIONED" - The runtime is no longer supported.
	//   "END_OF_SUPPORT" - The runtime is end of support.
	Stage string `json:"stage,omitempty"`
	// SupportedOperatingSystems: Supported operating systems for the runtime,
	// e.g., 'ubuntu22', etc.
	SupportedOperatingSystems []string `json:"supportedOperatingSystems,omitempty"`
	// Warnings: Warning messages, e.g., a deprecation warning.
	Warnings []string `json:"warnings,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DecommissionedDate") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DecommissionedDate") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Runtime: Runtime versions for App Engine.

func (Runtime) MarshalJSON ¶
added in v0.137.0
func (s Runtime) MarshalJSON() ([]byte, error)
type ScriptHandler ¶
type ScriptHandler struct {
	// ScriptPath: Path to the script from the application root directory.
	ScriptPath string `json:"scriptPath,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ScriptPath") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ScriptPath") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ScriptHandler: Executes a script to handle the request that matches the URL pattern.

func (ScriptHandler) MarshalJSON ¶
func (s ScriptHandler) MarshalJSON() ([]byte, error)
type Service ¶
type Service struct {
	// GeneratedCustomerMetadata: Additional Google Generated Customer Metadata,
	// this field won't be provided by default and can be requested by setting the
	// IncludeExtraData field in GetServiceRequest
	GeneratedCustomerMetadata googleapi.RawMessage `json:"generatedCustomerMetadata,omitempty"`
	// Id: Output only. Relative name of the service within the application.
	// Example: default.@OutputOnly
	Id string `json:"id,omitempty"`
	// Labels: A set of labels to apply to this service. Labels are key/value pairs
	// that describe the service and all resources that belong to it (e.g.,
	// versions). The labels can be used to search and group resources, and are
	// propagated to the usage and billing reports, enabling fine-grain analysis of
	// costs. An example of using labels is to tag resources belonging to different
	// environments (e.g., "env=prod", "env=qa"). Label keys and values can be no
	// longer than 63 characters and can only contain lowercase letters, numeric
	// characters, underscores, dashes, and international characters. Label keys
	// must start with a lowercase letter or an international character. Each
	// service can have at most 32 labels.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Output only. Full path to the Service resource in the API. Example:
	// apps/myapp/services/default.@OutputOnly
	Name string `json:"name,omitempty"`
	// NetworkSettings: Ingress settings for this service. Will apply to all
	// versions.
	NetworkSettings *NetworkSettings `json:"networkSettings,omitempty"`
	// Split: Mapping that defines fractional HTTP traffic diversion to different
	// versions within the service.
	Split *TrafficSplit `json:"split,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "GeneratedCustomerMetadata")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GeneratedCustomerMetadata") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Service: A Service resource is a logical component of an application that can share state and communicate in a secure fashion with other services. For example, an application that handles customer requests might include separate services to handle tasks such as backend data analysis or API requests from mobile devices. Each service has a collection of versions that define a specific set of code used to implement the functionality of that service.

func (Service) MarshalJSON ¶
func (s Service) MarshalJSON() ([]byte, error)
type SslSettings ¶
type SslSettings struct {
	// CertificateId: ID of the AuthorizedCertificate resource configuring SSL for
	// the application. Clearing this field will remove SSL support.By default, a
	// managed certificate is automatically created for every domain mapping. To
	// omit SSL support or to configure SSL manually, specify
	// SslManagementType.MANUAL on a CREATE or UPDATE request. You must be
	// authorized to administer the AuthorizedCertificate resource to manually map
	// it to a DomainMapping resource. Example: 12345.
	CertificateId string `json:"certificateId,omitempty"`
	// PendingManagedCertificateId: Output only. ID of the managed
	// AuthorizedCertificate resource currently being provisioned, if applicable.
	// Until the new managed certificate has been successfully provisioned, the
	// previous SSL state will be preserved. Once the provisioning process
	// completes, the certificate_id field will reflect the new managed certificate
	// and this field will be left empty. To remove SSL support while there is
	// still a pending managed certificate, clear the certificate_id field with an
	// UpdateDomainMappingRequest.@OutputOnly
	PendingManagedCertificateId string `json:"pendingManagedCertificateId,omitempty"`
	// SslManagementType: SSL management type for this domain. If AUTOMATIC, a
	// managed certificate is automatically provisioned. If MANUAL, certificate_id
	// must be manually specified in order to configure SSL for this domain.
	//
	// Possible values:
	//   "AUTOMATIC" - SSL support for this domain is configured automatically. The
	// mapped SSL certificate will be automatically renewed.
	//   "MANUAL" - SSL support for this domain is configured manually by the user.
	// Either the domain has no SSL support or a user-obtained SSL certificate has
	// been explicitly mapped to this domain.
	SslManagementType string `json:"sslManagementType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CertificateId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CertificateId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SslSettings: SSL configuration for a DomainMapping resource.

func (SslSettings) MarshalJSON ¶
func (s SslSettings) MarshalJSON() ([]byte, error)
type StandardSchedulerSettings ¶
type StandardSchedulerSettings struct {
	// MaxInstances: Maximum number of instances to run for this version. Set to
	// 2147483647 to disable max_instances configuration.
	MaxInstances int64 `json:"maxInstances,omitempty"`
	// MinInstances: Minimum number of instances to run for this version. Set to
	// zero to disable min_instances configuration.
	MinInstances int64 `json:"minInstances,omitempty"`
	// TargetCpuUtilization: Target CPU utilization ratio to maintain when scaling.
	TargetCpuUtilization float64 `json:"targetCpuUtilization,omitempty"`
	// TargetThroughputUtilization: Target throughput utilization ratio to maintain
	// when scaling
	TargetThroughputUtilization float64 `json:"targetThroughputUtilization,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MaxInstances") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MaxInstances") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StandardSchedulerSettings: Scheduler settings for standard environment.

func (StandardSchedulerSettings) MarshalJSON ¶
func (s StandardSchedulerSettings) MarshalJSON() ([]byte, error)
func (*StandardSchedulerSettings) UnmarshalJSON ¶
func (s *StandardSchedulerSettings) UnmarshalJSON(data []byte) error
type StaticFilesHandler ¶
type StaticFilesHandler struct {
	// ApplicationReadable: Whether files should also be uploaded as code data. By
	// default, files declared in static file handlers are uploaded as static data
	// and are only served to end users; they cannot be read by the application. If
	// enabled, uploads are charged against both your code and static data storage
	// resource quotas.
	ApplicationReadable bool `json:"applicationReadable,omitempty"`
	// Expiration: Time a static file served by this handler should be cached by
	// web proxies and browsers.
	Expiration string `json:"expiration,omitempty"`
	// HttpHeaders: HTTP headers to use for all responses from these URLs.
	HttpHeaders map[string]string `json:"httpHeaders,omitempty"`
	// MimeType: MIME type used to serve all files served by this handler.Defaults
	// to file-specific MIME types, which are derived from each file's filename
	// extension.
	MimeType string `json:"mimeType,omitempty"`
	// Path: Path to the static files matched by the URL pattern, from the
	// application root directory. The path can refer to text matched in groupings
	// in the URL pattern.
	Path string `json:"path,omitempty"`
	// RequireMatchingFile: Whether this handler should match the request if the
	// file referenced by the handler does not exist.
	RequireMatchingFile bool `json:"requireMatchingFile,omitempty"`
	// UploadPathRegex: Regular expression that matches the file paths for all
	// files that should be referenced by this handler.
	UploadPathRegex string `json:"uploadPathRegex,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApplicationReadable") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplicationReadable") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StaticFilesHandler: Files served directly to the user for a given URL, such as images, CSS stylesheets, or JavaScript source files. Static file handlers describe which files in the application directory are static files, and which URLs serve them.

func (StaticFilesHandler) MarshalJSON ¶
func (s StaticFilesHandler) MarshalJSON() ([]byte, error)
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

Status: The Status type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by gRPC (https://github.com/grpc). Each Status message contains three pieces of data: error code, error message, and error details.You can find out more about this error model and how to work with it in the API Design Guide (https://cloud.google.com/apis/design/errors).

func (Status) MarshalJSON ¶
func (s Status) MarshalJSON() ([]byte, error)
type TrafficSplit ¶
type TrafficSplit struct {
	// Allocations: Mapping from version IDs within the service to fractional
	// (0.000, 1] allocations of traffic for that version. Each version can be
	// specified only once, but some versions in the service may not have any
	// traffic allocation. Services that have traffic allocated cannot be deleted
	// until either the service is deleted or their traffic allocation is removed.
	// Allocations must sum to 1. Up to two decimal place precision is supported
	// for IP-based splits and up to three decimal places is supported for
	// cookie-based splits.
	Allocations map[string]float64 `json:"allocations,omitempty"`
	// ShardBy: Mechanism used to determine which version a request is sent to. The
	// traffic selection algorithm will be stable for either type until allocations
	// are changed.
	//
	// Possible values:
	//   "UNSPECIFIED" - Diversion method unspecified.
	//   "COOKIE" - Diversion based on a specially named cookie, "GOOGAPPUID." The
	// cookie must be set by the application itself or no diversion will occur.
	//   "IP" - Diversion based on applying the modulus operation to a fingerprint
	// of the IP address.
	//   "RANDOM" - Diversion based on weighted random assignment. An incoming
	// request is randomly routed to a version in the traffic split, with
	// probability proportional to the version's traffic share.
	ShardBy string `json:"shardBy,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Allocations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Allocations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TrafficSplit: Traffic routing configuration for versions within a single service. Traffic splits define how traffic directed to the service is assigned to versions.

func (TrafficSplit) MarshalJSON ¶
func (s TrafficSplit) MarshalJSON() ([]byte, error)
type UrlDispatchRule ¶
type UrlDispatchRule struct {
	// Domain: Domain name to match against. The wildcard "*" is supported if
	// specified before a period: "*.".Defaults to matching all domains: "*".
	Domain string `json:"domain,omitempty"`
	// Path: Pathname within the host. Must start with a "/". A single "*" can be
	// included at the end of the path.The sum of the lengths of the domain and
	// path may not exceed 100 characters.
	Path string `json:"path,omitempty"`
	// Service: Resource ID of a service in this application that should serve the
	// matched request. The service must already exist. Example: default.
	Service string `json:"service,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Domain") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Domain") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UrlDispatchRule: Rules to match an HTTP request and dispatch that request to a service.

func (UrlDispatchRule) MarshalJSON ¶
func (s UrlDispatchRule) MarshalJSON() ([]byte, error)
type UrlMap ¶
type UrlMap struct {
	// ApiEndpoint: Uses API Endpoints to handle requests.
	ApiEndpoint *ApiEndpointHandler `json:"apiEndpoint,omitempty"`
	// AuthFailAction: Action to take when users access resources that require
	// authentication. Defaults to redirect.
	//
	// Possible values:
	//   "AUTH_FAIL_ACTION_UNSPECIFIED" - Not specified. AUTH_FAIL_ACTION_REDIRECT
	// is assumed.
	//   "AUTH_FAIL_ACTION_REDIRECT" - Redirects user to "accounts.google.com". The
	// user is redirected back to the application URL after signing in or creating
	// an account.
	//   "AUTH_FAIL_ACTION_UNAUTHORIZED" - Rejects request with a 401 HTTP status
	// code and an error message.
	AuthFailAction string `json:"authFailAction,omitempty"`
	// Login: Level of login required to access this resource. Not supported for
	// Node.js in the App Engine standard environment.
	//
	// Possible values:
	//   "LOGIN_UNSPECIFIED" - Not specified. LOGIN_OPTIONAL is assumed.
	//   "LOGIN_OPTIONAL" - Does not require that the user is signed in.
	//   "LOGIN_ADMIN" - If the user is not signed in, the auth_fail_action is
	// taken. In addition, if the user is not an administrator for the application,
	// they are given an error message regardless of auth_fail_action. If the user
	// is an administrator, the handler proceeds.
	//   "LOGIN_REQUIRED" - If the user has signed in, the handler proceeds
	// normally. Otherwise, the auth_fail_action is taken.
	Login string `json:"login,omitempty"`
	// RedirectHttpResponseCode: 30x code to use when performing redirects for the
	// secure field. Defaults to 302.
	//
	// Possible values:
	//   "REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED" - Not specified. 302 is assumed.
	//   "REDIRECT_HTTP_RESPONSE_CODE_301" - 301 Moved Permanently code.
	//   "REDIRECT_HTTP_RESPONSE_CODE_302" - 302 Moved Temporarily code.
	//   "REDIRECT_HTTP_RESPONSE_CODE_303" - 303 See Other code.
	//   "REDIRECT_HTTP_RESPONSE_CODE_307" - 307 Temporary Redirect code.
	RedirectHttpResponseCode string `json:"redirectHttpResponseCode,omitempty"`
	// Script: Executes a script to handle the requests that match this URL
	// pattern. Only the auto value is supported for Node.js in the App Engine
	// standard environment, for example "script": "auto".
	Script *ScriptHandler `json:"script,omitempty"`
	// SecurityLevel: Security (HTTPS) enforcement for this URL.
	//
	// Possible values:
	//   "SECURE_UNSPECIFIED" - Not specified.
	//   "SECURE_DEFAULT" - Both HTTP and HTTPS requests with URLs that match the
	// handler succeed without redirects. The application can examine the request
	// to determine which protocol was used, and respond accordingly.
	//   "SECURE_NEVER" - Requests for a URL that match this handler that use HTTPS
	// are automatically redirected to the HTTP equivalent URL.
	//   "SECURE_OPTIONAL" - Both HTTP and HTTPS requests with URLs that match the
	// handler succeed without redirects. The application can examine the request
	// to determine which protocol was used and respond accordingly.
	//   "SECURE_ALWAYS" - Requests for a URL that match this handler that do not
	// use HTTPS are automatically redirected to the HTTPS URL with the same path.
	// Query parameters are reserved for the redirect.
	SecurityLevel string `json:"securityLevel,omitempty"`
	// StaticFiles: Returns the contents of a file, such as an image, as the
	// response.
	StaticFiles *StaticFilesHandler `json:"staticFiles,omitempty"`
	// UrlRegex: URL prefix. Uses regular expression syntax, which means regexp
	// special characters must be escaped, but should not contain groupings. All
	// URLs that begin with this prefix are handled by this handler, using the
	// portion of the URL after the prefix as part of the file path.
	UrlRegex string `json:"urlRegex,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiEndpoint") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiEndpoint") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UrlMap: URL pattern and description of how the URL should be handled. App Engine can handle URLs by executing application code or by serving static files uploaded with the version, such as images, CSS, or JavaScript.

func (UrlMap) MarshalJSON ¶
func (s UrlMap) MarshalJSON() ([]byte, error)
type Version ¶
type Version struct {
	// ApiConfig: Serving configuration for Google Cloud Endpoints
	// (https://cloud.google.com/endpoints).Only returned in GET requests if
	// view=FULL is set.
	ApiConfig *ApiConfigHandler `json:"apiConfig,omitempty"`
	// AppEngineApis: Allows App Engine second generation runtimes to access the
	// legacy bundled services.
	AppEngineApis bool `json:"appEngineApis,omitempty"`
	// AppEngineBundledServices: List of specific App Engine Bundled Services that
	// are enabled for this Version.
	//
	// Possible values:
	//   "BUNDLED_SERVICE_TYPE_UNSPECIFIED" - Default, invalid value
	//   "BUNDLED_SERVICE_TYPE_APP_IDENTITY_SERVICE" - App Identity Service
	//   "BUNDLED_SERVICE_TYPE_BLOBSTORE" - Blobstore
	//   "BUNDLED_SERVICE_TYPE_CAPABILITY_SERVICE" - Capability Service
	//   "BUNDLED_SERVICE_TYPE_DATASTORE_V3" - Datastore V3
	//   "BUNDLED_SERVICE_TYPE_DEFERRED" - Deferred
	//   "BUNDLED_SERVICE_TYPE_IMAGES" - Images
	//   "BUNDLED_SERVICE_TYPE_MAIL" - Mail
	//   "BUNDLED_SERVICE_TYPE_MEMCACHE" - Memcache
	//   "BUNDLED_SERVICE_TYPE_MODULES" - Modules
	//   "BUNDLED_SERVICE_TYPE_NAMESPACES" - Namespaces
	//   "BUNDLED_SERVICE_TYPE_NDB" - NDB
	//   "BUNDLED_SERVICE_TYPE_SEARCH" - Search
	//   "BUNDLED_SERVICE_TYPE_TASKQUEUES" - Task Queues
	//   "BUNDLED_SERVICE_TYPE_URLFETCH" - URL Fetch
	//   "BUNDLED_SERVICE_TYPE_USERS" - Users
	AppEngineBundledServices []string `json:"appEngineBundledServices,omitempty"`
	// AutomaticScaling: Automatic scaling is based on request rate, response
	// latencies, and other application metrics. Instances are dynamically created
	// and destroyed as needed in order to handle traffic.
	AutomaticScaling *AutomaticScaling `json:"automaticScaling,omitempty"`
	// BasicScaling: A service with basic scaling will create an instance when the
	// application receives a request. The instance will be turned down when the
	// app becomes idle. Basic scaling is ideal for work that is intermittent or
	// driven by user activity.
	BasicScaling *BasicScaling `json:"basicScaling,omitempty"`
	// BetaSettings: Metadata settings that are supplied to this version to enable
	// beta runtime features.
	BetaSettings map[string]string `json:"betaSettings,omitempty"`
	// BuildEnvVariables: Environment variables available to the build
	// environment.Only returned in GET requests if view=FULL is set.
	BuildEnvVariables map[string]string `json:"buildEnvVariables,omitempty"`
	// CreateTime: Time that this version was created.@OutputOnly
	CreateTime string `json:"createTime,omitempty"`
	// CreatedBy: Output only. Email address of the user who created this
	// version.@OutputOnly
	CreatedBy string `json:"createdBy,omitempty"`
	// DefaultExpiration: Duration that static files should be cached by web
	// proxies and browsers. Only applicable if the corresponding
	// StaticFilesHandler
	// (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions#StaticFilesHandler)
	// does not specify its own expiration time.Only returned in GET requests if
	// view=FULL is set.
	DefaultExpiration string `json:"defaultExpiration,omitempty"`
	// Deployment: Code and application artifacts that make up this version.Only
	// returned in GET requests if view=FULL is set.
	Deployment *Deployment `json:"deployment,omitempty"`
	// DiskUsageBytes: Output only. Total size in bytes of all the files that are
	// included in this version and currently hosted on the App Engine
	// disk.@OutputOnly
	DiskUsageBytes int64 `json:"diskUsageBytes,omitempty,string"`
	// EndpointsApiService: Cloud Endpoints configuration.If endpoints_api_service
	// is set, the Cloud Endpoints Extensible Service Proxy will be provided to
	// serve the API implemented by the app.
	EndpointsApiService *EndpointsApiService `json:"endpointsApiService,omitempty"`
	// Entrypoint: The entrypoint for the application.
	Entrypoint *Entrypoint `json:"entrypoint,omitempty"`
	// Env: App Engine execution environment for this version.Defaults to standard.
	Env string `json:"env,omitempty"`
	// EnvVariables: Environment variables available to the application.Only
	// returned in GET requests if view=FULL is set.
	EnvVariables map[string]string `json:"envVariables,omitempty"`
	// ErrorHandlers: Custom static error pages. Limited to 10KB per page.Only
	// returned in GET requests if view=FULL is set.
	ErrorHandlers []*ErrorHandler `json:"errorHandlers,omitempty"`
	// FlexibleRuntimeSettings: Settings for App Engine flexible runtimes.
	FlexibleRuntimeSettings *FlexibleRuntimeSettings `json:"flexibleRuntimeSettings,omitempty"`
	// GeneratedCustomerMetadata: Additional Google Generated Customer Metadata,
	// this field won't be provided by default and can be requested by setting the
	// IncludeExtraData field in GetVersionRequest
	GeneratedCustomerMetadata googleapi.RawMessage `json:"generatedCustomerMetadata,omitempty"`
	// Handlers: An ordered list of URL-matching patterns that should be applied to
	// incoming requests. The first matching URL handles the request and other
	// request handlers are not attempted.Only returned in GET requests if
	// view=FULL is set.
	Handlers []*UrlMap `json:"handlers,omitempty"`
	// HealthCheck: Configures health checking for instances. Unhealthy instances
	// are stopped and replaced with new instances. Only applicable in the App
	// Engine flexible environment.
	HealthCheck *HealthCheck `json:"healthCheck,omitempty"`
	// Id: Relative name of the version within the service. Example: v1. Version
	// names can contain only lowercase letters, numbers, or hyphens. Reserved
	// names: "default", "latest", and any name with the prefix "ah-".
	Id string `json:"id,omitempty"`
	// InboundServices: Before an application can receive email or XMPP messages,
	// the application must be configured to enable the service.
	//
	// Possible values:
	//   "INBOUND_SERVICE_UNSPECIFIED" - Not specified.
	//   "INBOUND_SERVICE_MAIL" - Allows an application to receive mail.
	//   "INBOUND_SERVICE_MAIL_BOUNCE" - Allows an application to receive
	// email-bound notifications.
	//   "INBOUND_SERVICE_XMPP_ERROR" - Allows an application to receive error
	// stanzas.
	//   "INBOUND_SERVICE_XMPP_MESSAGE" - Allows an application to receive instant
	// messages.
	//   "INBOUND_SERVICE_XMPP_SUBSCRIBE" - Allows an application to receive user
	// subscription POSTs.
	//   "INBOUND_SERVICE_XMPP_PRESENCE" - Allows an application to receive a
	// user's chat presence.
	//   "INBOUND_SERVICE_CHANNEL_PRESENCE" - Registers an application for
	// notifications when a client connects or disconnects from a channel.
	//   "INBOUND_SERVICE_WARMUP" - Enables warmup requests.
	InboundServices []string `json:"inboundServices,omitempty"`
	// InstanceClass: Instance class that is used to run this version. Valid values
	// are: AutomaticScaling: F1, F2, F4, F4_1G ManualScaling or BasicScaling: B1,
	// B2, B4, B8, B4_1GDefaults to F1 for AutomaticScaling and B1 for
	// ManualScaling or BasicScaling.
	InstanceClass string `json:"instanceClass,omitempty"`
	// Libraries: Configuration for third-party Python runtime libraries that are
	// required by the application.Only returned in GET requests if view=FULL is
	// set.
	Libraries []*Library `json:"libraries,omitempty"`
	// LivenessCheck: Configures liveness health checking for instances. Unhealthy
	// instances are stopped and replaced with new instances
	LivenessCheck *LivenessCheck `json:"livenessCheck,omitempty"`
	// ManualScaling: A service with manual scaling runs continuously, allowing you
	// to perform complex initialization and rely on the state of its memory over
	// time. Manually scaled versions are sometimes referred to as "backends".
	ManualScaling *ManualScaling `json:"manualScaling,omitempty"`
	// Name: Output only. Full path to the Version resource in the API. Example:
	// apps/myapp/services/default/versions/v1.@OutputOnly
	Name string `json:"name,omitempty"`
	// Network: Extra network settings. Only applicable in the App Engine flexible
	// environment.
	Network *Network `json:"network,omitempty"`
	// NobuildFilesRegex: Files that match this pattern will not be built into this
	// version. Only applicable for Go runtimes.Only returned in GET requests if
	// view=FULL is set.
	NobuildFilesRegex string `json:"nobuildFilesRegex,omitempty"`
	// ReadinessCheck: Configures readiness health checking for instances.
	// Unhealthy instances are not put into the backend traffic rotation.
	ReadinessCheck *ReadinessCheck `json:"readinessCheck,omitempty"`
	// Resources: Machine resources for this version. Only applicable in the App
	// Engine flexible environment.
	Resources *Resources `json:"resources,omitempty"`
	// Runtime: Desired runtime. Example: python27.
	Runtime string `json:"runtime,omitempty"`
	// RuntimeApiVersion: The version of the API in the given runtime environment.
	// Please see the app.yaml reference for valid values at
	// https://cloud.google.com/appengine/docs/standard//config/appref
	RuntimeApiVersion string `json:"runtimeApiVersion,omitempty"`
	// RuntimeChannel: The channel of the runtime to use. Only available for some
	// runtimes. Defaults to the default channel.
	RuntimeChannel string `json:"runtimeChannel,omitempty"`
	// RuntimeMainExecutablePath: The path or name of the app's main executable.
	RuntimeMainExecutablePath string `json:"runtimeMainExecutablePath,omitempty"`
	// ServiceAccount: The identity that the deployed version will run as. Admin
	// API will use the App Engine Appspot service account as default if this field
	// is neither provided in app.yaml file nor through CLI flag.
	ServiceAccount string `json:"serviceAccount,omitempty"`
	// ServingStatus: Current serving status of this version. Only the versions
	// with a SERVING status create instances and can be
	// billed.SERVING_STATUS_UNSPECIFIED is an invalid value. Defaults to SERVING.
	//
	// Possible values:
	//   "SERVING_STATUS_UNSPECIFIED" - Not specified.
	//   "SERVING" - Currently serving. Instances are created according to the
	// scaling settings of the version.
	//   "STOPPED" - Disabled. No instances will be created and the scaling
	// settings are ignored until the state of the version changes to SERVING.
	ServingStatus string `json:"servingStatus,omitempty"`
	// Threadsafe: Whether multiple requests can be dispatched to this version at
	// once.
	Threadsafe bool `json:"threadsafe,omitempty"`
	// VersionUrl: Output only. Serving URL for this version. Example:
	// "https://myversion-dot-myservice-dot-myapp.appspot.com"@OutputOnly
	VersionUrl string `json:"versionUrl,omitempty"`
	// Vm: Whether to deploy this version in a container on a virtual machine.
	Vm bool `json:"vm,omitempty"`
	// VpcAccess: Enables VPC access connectivity for standard apps.
	VpcAccess *VpcAccess `json:"vpcAccess,omitempty"`
	// VpcAccessConnector: Enables VPC connectivity for standard apps.
	VpcAccessConnector *VpcAccessConnector `json:"vpcAccessConnector,omitempty"`
	// Zones: The Google Compute Engine zones that are supported by this version in
	// the App Engine flexible environment. Deprecated.
	Zones []string `json:"zones,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiConfig") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Version: A Version resource is a specific set of source code and configuration files that are deployed into a service.

func (Version) MarshalJSON ¶
func (s Version) MarshalJSON() ([]byte, error)
type Volume ¶
type Volume struct {
	// Name: Unique name for the volume.
	Name string `json:"name,omitempty"`
	// SizeGb: Volume size in gigabytes.
	SizeGb float64 `json:"sizeGb,omitempty"`
	// VolumeType: Underlying volume type, e.g. 'tmpfs'.
	VolumeType string `json:"volumeType,omitempty"`
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

Volume: Volumes mounted within the app container. Only applicable in the App Engine flexible environment.

func (Volume) MarshalJSON ¶
func (s Volume) MarshalJSON() ([]byte, error)
func (*Volume) UnmarshalJSON ¶
func (s *Volume) UnmarshalJSON(data []byte) error
type VpcAccess ¶
added in v0.261.0
type VpcAccess struct {
	// NetworkInterfaces: The Direct VPC configuration. Currently only single
	// network interface is supported.
	NetworkInterfaces []*VpcNetworkInterface `json:"networkInterfaces,omitempty"`
	// VpcEgress: The traffic egress setting for the VPC network interface,
	// controlling what traffic is diverted through it.
	//
	// Possible values:
	//   "VPC_EGRESS_UNSPECIFIED" - No value set; apply default behavior
	//   "ALL_TRAFFIC" - Force all traffic to egress through the NetworkInterface
	// (and configured VPC Network)
	//   "PRIVATE_IP_RANGES" - Force all Private IP Space traffic to egress through
	// NetworkInterface (and configured VPC Network)
	VpcEgress string `json:"vpcEgress,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NetworkInterfaces") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NetworkInterfaces") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VpcAccess: VPC Access settings

func (VpcAccess) MarshalJSON ¶
added in v0.261.0
func (s VpcAccess) MarshalJSON() ([]byte, error)
type VpcAccessConnector ¶
type VpcAccessConnector struct {
	// EgressSetting: The egress setting for the connector, controlling what
	// traffic is diverted through it.
	//
	// Possible values:
	//   "EGRESS_SETTING_UNSPECIFIED"
	//   "ALL_TRAFFIC" - Force the use of VPC Access for all egress traffic from
	// the function.
	//   "PRIVATE_IP_RANGES" - Use the VPC Access Connector for private IP space
	// from RFC1918.
	EgressSetting string `json:"egressSetting,omitempty"`
	// Name: Full Serverless VPC Access Connector name e.g.
	// projects/my-project/locations/us-central1/connectors/c1.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EgressSetting") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EgressSetting") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VpcAccessConnector: VPC access connector specification.

func (VpcAccessConnector) MarshalJSON ¶
func (s VpcAccessConnector) MarshalJSON() ([]byte, error)
type VpcNetworkInterface ¶
added in v0.261.0
type VpcNetworkInterface struct {
	// Network: Optional. The VPC network that the App Engine resource will be able
	// to send traffic to. At least one of network or subnetwork must be specified.
	// If both network and subnetwork are specified, the given VPC subnetwork must
	// belong to the given VPC network. If network is not specified, it will be
	// looked up from the subnetwork. Could be either a short name or a full path.
	// e.g. {VPC_NETWORK} or
	// projects/{HOST_PROJECT_ID}/global/networks/{VPC_NETWORK}
	Network string `json:"network,omitempty"`
	// Subnet: Optional. The VPC subnetwork that the App Engine resource will get
	// IPs from. At least one of network or subnetwork must be specified. If both
	// network and subnetwork are specified, the given VPC subnetwork must belong
	// to the given VPC network. If subnetwork is not specified, the subnetwork
	// with the same name with the network will be used. Could be either a short
	// name or a full path. e.g. {SUBNET_NAME} or
	// projects/{HOST_PROJECT_ID}/regions/{REGION}/subnetworks/{SUBNET_NAME}
	Subnet string `json:"subnet,omitempty"`
	// Tags: Optional. The network tags that will be applied to this App Engine
	// resource.
	Tags []string `json:"tags,omitempty"`
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

VpcNetworkInterface: Network interface key message.

func (VpcNetworkInterface) MarshalJSON ¶
added in v0.261.0
func (s VpcNetworkInterface) MarshalJSON() ([]byte, error)
type ZipInfo ¶
type ZipInfo struct {
	// FilesCount: An estimate of the number of files in a zip for a zip
	// deployment. If set, must be greater than or equal to the actual number of
	// files. Used for optimizing performance; if not provided, deployment may be
	// slow.
	FilesCount int64 `json:"filesCount,omitempty"`
	// SourceUrl: URL of the zip file to deploy from. Must be a URL to a resource
	// in Google Cloud Storage in the form 'http(s)://storage.googleapis.com//'.
	SourceUrl string `json:"sourceUrl,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FilesCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilesCount") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ZipInfo: The zip file information for a zip deployment.

func (ZipInfo) MarshalJSON ¶
func (s ZipInfo) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
appengine-gen.go
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
